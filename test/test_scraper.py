from src.scraper import JobData


def test_webdriver():
    job_obj = JobData()
    job_obj.setup_webdriver()
    job_obj.driver.quit()
