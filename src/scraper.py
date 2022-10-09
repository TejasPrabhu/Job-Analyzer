import os
import sys
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
from app import add, mongodb_client
db = mongodb_client.db

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))


class JobData:
    def __init__(self,
                 job_title="Software Engineer",
                 job_location="Raleigh",
                 distance=20,
                 company="",
                 number_jobs=10,
                 df=None) -> None:
        self.driver = None
        self.job_data = df
        self.job_title = job_title,
        self.job_location = job_location,
        self.distance = distance,
        self.company = company,
        self.number_jobs = number_jobs
        self.skills = ['python', 'c', 'r', 'c++', 'java', 'hadoop', 'scala', 'flask', 'pandas', 'spark', 'scikit-learn',
                       'numpy', 'php', 'sql', 'mysql', 'css', 'mongdb', 'nltk', 'fastai', 'keras', 'pytorch',
                       'tensorflow', 'linux', 'Ruby', 'JavaScript', 'django', 'react', 'reactjs', 'ai', 'ui', 'tableau']

    def setup_webdriver(self):
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

        chrome_options = Options()
        options = [
            "--headless",
            "--disable-gpu",
            "--window-size=1920,1200",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)

        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def scroll_to_end(self):
        while True:

            try:
                self.driver.find_element(By.CLASS_NAME, 'results-context-header__job-count').click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'infinite-scroller__show-more-button')))
                break

            except BaseException:
                pass

    def scrape_job_details(self, df, job):
        try:

            job.click()
            time.sleep(1)

            job_info = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "two-pane-serp-page__detail-view")))
            time.sleep(1)
            WebDriverWait(job_info, 3).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'show-more-less-html__button'))).click()

            job_title = job_info.find_element(By.CLASS_NAME, 'topcard__title').text
            company_name = job_info.find_element(By.CLASS_NAME, 'topcard__org-name-link').text
            location = job_info.find_element(By.CLASS_NAME, 'topcard__flavor-row').text.lstrip(company_name)
            posted = job_info.find_element(By.CLASS_NAME, 'posted-time-ago__text').text
            applicants = job_info.find_element(By.CLASS_NAME, 'num-applicants__caption').text
            job_desc = job_info.find_element(By.CLASS_NAME, 'show-more-less-html__markup').text
            job_link = job_info.find_element(By.CLASS_NAME, 'apply-button').get_attribute('href')

            job_dict = {
                'Job Title': job_title,
                'Company Name': company_name,
                'Location': location,
                'Date Posted': posted,
                'Total Applicants': applicants,
                'Job Description': job_desc,
                'Job Link': job_link
            }

            job_criteria = job_info.find_element(By.CLASS_NAME, 'description__job-criteria-list').text.split('\n')

            if job_criteria:
                j = 0

                while j < (len(job_criteria)):
                    if job_criteria[j] in list(df.columns):
                        job_dict[job_criteria[j]] = job_criteria[j + 1]
                        j += 2

            df = df.append(job_dict, ignore_index=True)
            time.sleep(1)
            return df

        except TimeoutException:
            return

    def linkedin_scraper(self, max_jobs=25):
        columns = [
            'Job Title',
            'Company Name',
            'Location',
            'Date Posted',
            'Total Applicants',
            'Job Description',
            'Job Link',
            'Seniority level',
            'Employment type',
            'Job function',
            'Industries']
        df = pd.DataFrame(columns=columns)

        i = 0

        try:

            while i < max_jobs:

                if self.driver.find_elements(By.CLASS_NAME, 'infinite-scroller__show-more-button'):
                    self.scroll_to_end()

                job_list = self.driver.find_element(
                    By.CLASS_NAME, 'jobs-search__results-list').find_elements(
                    By.CLASS_NAME, 'job-search-card')

                job_list = job_list[i:max_jobs] if len(job_list) > max_jobs else job_list[i:]

                if not job_list:
                    break

                for job in job_list:
                    ret_val = self.scrape_job_details(df, job)

                    if ret_val is not None:
                        df = ret_val

                if self.driver.find_elements(By.CLASS_NAME, 'infinite-scroller__show-more-button'):
                    self.driver.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button').click()
                    WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.CLASS_NAME, 'infinite-scroller__show-more-button')))

                i += len(job_list)

        except Exception:
            print(traceback.format_exc())
            sys.exit(1)

        return df

    def get_linkedin_url(self):

        url = "https://www.linkedin.com/jobs/search?keywords={} {}&location={}&distance={}" \
            .format(self.job_title, self.company, self.job_location, self.distance)
        return url

    def scrape_data(self, save_csv=True):
        url = self.get_linkedin_url()
        self.setup_webdriver()
        self.driver.get(url)
        try:
            self.job_data = self.linkedin_scraper(max_jobs=self.number_jobs)
            self.extract_skill()

            if save_csv:
                self.job_data.to_csv(os.path.join(ROOT_DIR, 'data', 'linkedin_scraper.csv'))

        finally:
            self.driver.close()

    def extract_skill(self):
        skill_list = list()
        for row in self.job_data['Job Description']:
            desc = row.lower()
            desc = [word.strip(',') for word in desc.split()]
            common_list = list(set(desc) & set(self.skills))
            skill_list.append(common_list)

        self.job_data['skills'] = skill_list

    def update_attributes(self, job_title="Software Engineer", job_location="Raleigh", distance=20,
                          company="", number_jobs=10):

        self.job_title = job_title
        self.job_location = job_location
        self.distance = distance
        self.company = company
        self.number_jobs = number_jobs

if __name__ == '__main__':
    jd = JobData()
    job_data = jd.scrape_data()
    add(db, job_data)
