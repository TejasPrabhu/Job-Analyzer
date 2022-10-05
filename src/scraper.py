import time
import traceback

import pandas as pd
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def setup_webdriver():
    chrome_service = Service(ChromeDriverManager(
        chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        # "--headless",
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


def scroll_to_end(driver):
    while True:

        try:
            driver.find_element(
                By.CLASS_NAME, 'results-context-header__job-count').click()
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            WebDriverWait(
                driver, 2).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, 'infinite-scroller__show-more-button')))
            break
        except BaseException:
            pass


def scrape_job_details(driver, df, job):
    try:

        job.click()
        time.sleep(1)

        job_info = WebDriverWait(
            driver, 2).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "two-pane-serp-page__detail-view")))
        time.sleep(1)
        WebDriverWait(
            job_info, 3).until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, 'show-more-less-html__button'))).click()

        job_title = job_info.find_element(By.CLASS_NAME, 'topcard__title').text
        company_name = job_info.find_element(
            By.CLASS_NAME, 'topcard__org-name-link').text
        location = job_info.find_element(
            By.CLASS_NAME, 'topcard__flavor-row').text.lstrip(company_name)
        posted = job_info.find_element(
            By.CLASS_NAME, 'posted-time-ago__text').text
        applicants = job_info.find_element(
            By.CLASS_NAME, 'num-applicants__caption').text
        job_desc = job_info.find_element(
            By.CLASS_NAME, 'show-more-less-html__markup').text

        job_dict = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Date Posted': posted,
            'Total Applicants': applicants,
            'Job Description': job_desc
        }

        job_criteria = job_info.find_element(
            By.CLASS_NAME, 'description__job-criteria-list').text.split('\n')

        if job_criteria:
            j = 0

            while j < (len(job_criteria)):
                if job_criteria[j] in list(df.columns):
                    job_dict[job_criteria[j]] = job_criteria[j + 1]
                    j += 2

        # print(job_dict)
        # df = df.append(job_dict, ignore_index=True)
        row_labels = [1]
        job_df = pd.DataFrame(data=job_dict, index=row_labels)
        df = pd.concat([df, job_df], ignore_index=True)
        time.sleep(1)
        return df

    except TimeoutException:
        return


def linkedin_scraper(driver, max_jobs=25):
    columns = [
        'Job Title',
        'Company Name',
        'Location',
        'Date Posted',
        'Total Applicants',
        'Job Description',
        'Seniority level',
        'Employment type',
        'Job function',
        'Industries']
    df = pd.DataFrame(columns=columns)

    i = 0

    try:

        while i < max_jobs:

            if driver.find_elements(
                    By.CLASS_NAME,
                    'infinite-scroller__show-more-button'):
                scroll_to_end(driver)

            job_list = driver.find_element(
                By.CLASS_NAME, 'jobs-search__results-list').find_elements(
                By.CLASS_NAME, 'job-search-card')

            if len(job_list) > max_jobs:
                job_list = job_list[i:max_jobs]
            else:
                job_list = job_list[i:]

            if not job_list:
                break

            for job in job_list:
                ret_val = scrape_job_details(driver, df, job)

                if ret_val is not None:
                    df = ret_val

            if driver.find_elements(
                    By.CLASS_NAME,
                    'infinite-scroller__show-more-button'):
                driver.find_element(
                    By.CLASS_NAME,
                    'infinite-scroller__show-more-button').click()
                WebDriverWait(
                    driver, 5).until(
                    EC.element_to_be_clickable(
                        (By.CLASS_NAME,
                            'infinite-scroller__show-more-button')))

            i += len(job_list)

    except Exception:
        print(traceback.format_exc())

    return df


def get_linkedin_url(
        job_title="Software Engineer",
        job_location="Raleigh",
        distance=20,
        company=""):

    url = "https://www.linkedin.com/jobs/search?keywords={}"\
        " {}&location={}&distance={}".format(
            job_title, company, job_location, distance)
    return url


def scrape_data(
        job_title="Software Engineer",
        job_location="Raleigh",
        distance=20,
        company="",
        number_jobs=40):
    url = get_linkedin_url(job_title, job_location, distance, company)
    wd = setup_webdriver()
    wd.get(url)
    jobs = linkedin_scraper(driver=wd, max_jobs=number_jobs)
    jobs.to_csv('../data/linkedin_scraper.csv')
    wd.quit()


def scrape_df(
        job_title,
        job_location,
        distance,
        company="",
        number_jobs=40):
    url = get_linkedin_url(job_title, job_location, distance, company)
    wd = setup_webdriver()
    wd.get(url)
    jobs = linkedin_scraper(driver=wd, max_jobs=number_jobs)
    wd.quit()
    return jobs
