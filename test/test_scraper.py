import pandas as pd

from src.scraper import JobData


def test_sample():
    assert True

def test_extract_skill():
    df = pd.read_csv('data/linkedin_scraper.csv')
    jd = JobData(df=df)
    jd.extract_skill()
    jd_df = jd.job_data
    assert (jd_df.iloc[0]['skills'].sort() == ['c++', 'sql', 'java', 'react', 'python', 'spark'].sort())
