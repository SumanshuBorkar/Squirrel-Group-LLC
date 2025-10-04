# 🕸️ Web Scraping Assignment — AEI Engineering Job Page

This project is a small **FastAPI** application that scrapes job details (title, job ID, location, and description) from the given AEI Engineering careers page using **Selenium** and **BeautifulSoup**.

---

## 🚀 Project Overview

**Task:**  
Scrape the following job page —  
[Engineering Data Analyst | AEI Careers](https://careers-aeieng.icims.com/jobs/5417/engineering-data-analyst/job)

**Goal:**  
Extract the following details:
- Job Title  
- Job ID  
- Job Location  
- Job Description  

**Tech Stack:**
- **Python 3.11**
- **FastAPI**
- **Selenium**
- **BeautifulSoup4**
- **Uvicorn** (for running the FastAPI server)

---

### 🧩 Project Structure

- web-scraper/
- │
- ├── main.py # Main FastAPI application with the scraping logic
- ├── requirements.txt
- └── README.md

---
```

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/SumanshuBorkar/Squirrel-Group-LLC.git

# setup

cd web-scraper

#  Most stable in pyhton 3.11
brew install pyenv
pyenv install 3.11
pyenv local 3.11

#  Setup the virtual environment
python3.11 -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

pip install -r requirements.txt 
uvicorn main:app --reload

# Access this endpoint to get the response 
http://127.0.0.1:8000/scrape


```
