import itertools
import time

from src.scraper import JobData


def test_webdriver():
    job_obj = JobData()
    job_obj.setup_webdriver()
    job_obj.driver.quit()


def test_linkedin_url():
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
