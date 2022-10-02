from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By

url = "https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Raleigh%2C%20North%20Carolina%2C%" \
      "20United%20States&geoId=100197101&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

columns = ['Job Title', 'Company Name', 'Location', 'Date Posted', 'Total Applicants', 'Seniority level',
           'Employment type', 'Job function', 'Industries']
df = pd.DataFrame(columns=columns)

wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)

job_list = wd.find_element(By.CLASS_NAME, 'jobs-search__results-list').find_elements(By.CLASS_NAME, 'job-search-card')

for job in job_list:

    job.click()
    time.sleep(5)

    job_info = wd.find_element(By.CLASS_NAME, 'two-pane-serp-page__detail-view')
    # job_info.find_element(By.CLASS_NAME, 'show-more-less-html__button').click()

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

df.to_csv('linkedin_scraper.csv')
