from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By

url = "https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Toronto%2C%20Ontario%2C%20Canada&geoId=100025096&trk=public_jobs_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0 "

columns = ['Job Title', 'Company Name', 'Location', 'Date Posted', 'Total Applicants', 'Seniority level',
           'Employment type', 'Job function', 'Industries']
df = pd.DataFrame(columns=columns)

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
wd = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
wd.get(url)

max_jobs = 100

i = 0

while i <= max_jobs:

    while True:

        try:
            wd.find_element(By.CLASS_NAME, 'results-context-header__job-count').click()
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            wd.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button').click()
            break
        except:
            pass

    job_list = wd.find_element(By.CLASS_NAME, 'jobs-search__results-list').find_elements(By.CLASS_NAME,
                                                                                         'job-search-card')[i:]

    for job in job_list:

        job.click()
        time.sleep(3)

        job_info = wd.find_element(By.CLASS_NAME, 'two-pane-serp-page__detail-view')
        job_info.find_element(By.CLASS_NAME, 'show-more-less-html__button').click()

        job_title = job_info.find_element(By.CLASS_NAME, 'topcard__title').text
        company_name = job_info.find_element(By.CLASS_NAME, 'topcard__org-name-link').text
        location = job_info.find_element(By.CLASS_NAME, 'topcard__flavor-row').text.lstrip(company_name)
        posted = job_info.find_element(By.CLASS_NAME, 'posted-time-ago__text').text
        applicants = job_info.find_element(By.CLASS_NAME, 'num-applicants__caption').text

        job_dict = {
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Date Posted': posted,
            'Total Applicants': applicants,
        }

        job_criteria = job_info.find_element(By.CLASS_NAME, 'description__job-criteria-list').text.split('\n')

        if job_criteria:
            j = 0

            while j < (len(job_criteria)):
                if job_criteria[j] in columns:
                    job_dict[job_criteria[j]] = job_criteria[j + 1]
                    j += 2

        df = df.append(job_dict, ignore_index=True)

    wd.find_element(By.CLASS_NAME, 'infinite-scroller__show-more-button').click()
    time.sleep(5)
    i += len(job_list)

df.to_csv('linkedin_scraper.csv')
