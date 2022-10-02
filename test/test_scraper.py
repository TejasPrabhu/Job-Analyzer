from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def setup():
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--start-maximized",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return driver


def test_scraper():
    url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Raleigh%2C%20North%20Carolina" \
          "%2C%20United%20States&geoId=100197101&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

    wd = setup()
    wd.get(url)
    jobs = wd.find_element(By.CLASS_NAME, 'jobs-search__results-list').find_elements(By.CLASS_NAME, 'job-search-card')
    wd.quit()
    print("Number of jobs {}".format(len(jobs)))

    assert len(jobs) > 0
