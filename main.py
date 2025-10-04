from fastapi import FastAPI
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI(title="Job Scraper API", version="1.1")

JOB_URL = "https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job?mobile=false&width=1920&height=500&bga=true&needsRedirect=false&jan1offset=330&jun1offset=330"

@app.get("/")
def home():
    return {"message": "Go to /scrape to fetch job details."}

@app.get("/scrape")
def scrape_job_details():
    """
    Uses Selenium to scrape job details from the dynamic iCIMS iframe.
    """
    try:
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        import time

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(JOB_URL)

        time.sleep(3)

        iframe = driver.find_element(By.ID, "icims_content_iframe")
        driver.switch_to.frame(iframe)

        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        title = soup.select_one("h1.iCIMS_Header")

        job_id, location = None, None
        header_tags = soup.select("div.iCIMS_JobHeaderTag")

        for tag in header_tags:
            label = tag.select_one("dt")
            value = tag.select_one("dd span")
            if not label or not value:
                continue

            label_text = label.get_text(strip=True).lower()
            value_text = value.get_text(strip=True)

            if "job id" in label_text:
                job_id = value_text
            elif "location" in label_text or "job location" in label_text:
                location = value_text

        description_div = soup.select_one("div.iCIMS_JobContent")

        driver.quit()

        return {
            "job_title": title.get_text(strip=True) if title else None,
            "job_id": job_id,
            "location": location,
            "description": description_div.get_text(strip=True, separator="\n") if description_div else None
        }

    except Exception as e:
        return {"error": str(e)}
