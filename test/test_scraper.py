"""
The test_scraper module holds testing functions.
"""
"""Copyright 2022 Tejas Prabhu

Use of this source code is governed by an MIT-style
license that can be found in the LICENSE file or at
https://opensource.org/licenses/MIT.
"""


import itertools  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402
import pandas as pd  # noqa: E402
from scraper import JobData, ROOT_DIR  # noqa: E402


def test_webdriver():
    """
    The function test_webdriver tests the Chrome Web Driver.
    """
    job_obj = JobData()
    job_obj.setup_webdriver()
    job_obj.driver.quit()


def test_linkedin_url():
    """
    The function test_linkedin_url tests if the url for scraping created correctly.
    """
    job_title_list = ["", "Data Scientist"]
    job_location_list = ["", "California"]
    distance_list = ["", 100]
    company_list = ["", "Amazon"]

    job_obj = JobData()
    job_obj.setup_webdriver()

    for job_title, job_location, distance, company in itertools.product(job_title_list, job_location_list,
                                                                        distance_list, company_list):
        job_obj.update_attributes(job_title=job_title, job_location=job_location, distance=distance,
                                  company=company)
        url = job_obj.get_linkedin_url()
        job_obj.driver.get(url)

        assert type(url) == str

        time.sleep(1)

    job_obj.driver.quit()


def test_scraper_zero_jobs():
    """
    The test_scraper_zero_jobs checks for number_jobs = 0
    """
    number_jobs = 0
    job_obj = JobData(number_jobs=number_jobs)
    job_obj.scrape_data(save_csv=False)


def test_update_attributes():
    """
    The test_update_attributes checks if the attributes are updated or not.
    """
    job_title = "Software Engineer"
    job_location = "Raleigh"
    distance = 20
    company = ""
    number_jobs = 10

    job_obj = JobData()
    job_obj.update_attributes(job_title=job_title, job_location=job_location, distance=distance, company=company,
                              number_jobs=number_jobs)

    assert job_obj.job_title == job_title
    assert job_obj.job_location == job_location
    assert job_obj.distance == distance
    assert job_obj.company == company
    assert job_obj.number_jobs == number_jobs


def test_extract_skill():
    """
    The test_extract_skill function checks if the skills are extracted properly from the job description.
    """
    csv_path = os.path.join(ROOT_DIR, 'data', 'linkedin_scraper.csv')
    df = pd.read_csv(csv_path)
    jd = JobData(df=df)
    jd.extract_skill()
    jd_df = jd.job_data
    assert (jd_df.iloc[0]['skills'].sort() == ['c++', 'sql', 'java', 'react', 'python', 'spark'].sort())
