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

## How does this works ?

- Below is the sequence diagram explaining the flow.

<p align="center">
  <img src="https://uml.planttext.com/plantuml/svg/TP9DJm8n48Rl_HKJJhi9nliU3AYW65J2GZYIeHsWfjis_K1_ljqlmffuc-syxplFJZln0Ls8bM911aKmHn-cgmNiw00bTsYbFi5ScM_6a0VZOEl9CPiyaakBEi2ejqoj7G7wFc8eQhB8bUGkabEZwux-w4YHbh62xEdiJ4NFJbx8vQsXwmqTZuGno6DKfOajG5qmLeF2tKEFKy3BR0FtlXdAUkRKxp0AQ5lxBtFO2meebSzordKROJU-W2L6pSzm9XIAl8SMbLtPXsA30gQp1QHWi7WYoBRhPVwFUeSom37jMHuTLWIeHMFiY8QkddnD8JhTXdiJ7ITutRml1_1f9mMiqFc-bmu68REVuD8LrzFspLiODwKKOr26Ov16ZnD6sfAqzSTj-dN77OaFBl9KaG210I4JaeVyTklrxHJmLdv-98-tHYUkxEP7SyOcf4NzC7y1" alt="Logo" width="100%"/>
</p>

- Below is the class Diagram explaining the interaction of different components and activities 

<p align="center">
  <img src="https://uml.planttext.com/plantuml/svg/RLBBJiCm4BpxArOzfQhw0psWbbO84D2A876qt6H9jt9Yoslt0EBViTrdK2v-xCwCPspFsIldGwk59wyHbbenmufKurGBK_Z4BPILKvQw1ZRExB7oGbGPDSeDT2Mw0rKuWXy1aL8xEg23MUAkyZgM9o0bTUIbBCQGzvp9Sc-siaQlI7CHd9u1UpUEv9hYGKckGI-jQb2o2Qx27YXE6MELOvGxt-eY3NsHtulV1yL-iNbQM7lqEW5bROITwZUsYiH-BjTlxyZMT8mtAYLgx2YqnsndfUNEcHRNrbE4HxBPvgkwjbRdQpbrheBtg8Adhw1B4-mcHRcevc33cQvXO3gzW_vRH5nWPF6lce4z-n6OdeMKfkzX_82xICh661u_Nb-4c6DNfo_q1m00"/>
</p>

