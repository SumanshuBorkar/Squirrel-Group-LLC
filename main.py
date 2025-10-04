from fastapi import FastAPI
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = FastAPI(title="Job Scraper API", version="1.1")

JOB_URL = "https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job"