from fastapi import FastAPI
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI(title="Job Scraper API", version="1.1")

JOB_URL = "https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job"

@app.get("/")
def home():
    return {"message": "Go to /scrape to fetch job details."}

@app.get("/scrape")
def scrape_job_details():
    """
    Uses Selenium to scrape job details from the dynamic page.
    """
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(JOB_URL)

        driver.implicitly_wait(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        title = soup.find("h1", class_="iCIMS_Header")
        job_id = soup.find("span", class_="iCIMS_JobNumber")
        location = soup.find("span", class_="iCIMS_JobHeaderFieldValue")
        description_div = soup.find("div", class_="iCIMS_JobContent")

        driver.quit()

        return {
            "job_title": title.get_text(strip=True) if title else None,
            "job_id": job_id.get_text(strip=True) if job_id else None,
            "location": location.get_text(strip=True) if location else None,
            "description": description_div.get_text(strip=True, separator="\n") if description_div else None
        }

    except Exception as e:
        return {"error": str(e)}
