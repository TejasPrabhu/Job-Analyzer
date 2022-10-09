import pandas as pd

from pathlib import Path
from src.scraper import JobData

csv_path = Path('data/linkedin_scraper.csv')


def test_sample():
    assert True


def test_extract_skill():
    df = pd.read_csv(csv_path)
    jd = JobData(df=df)
    jd.extract_skill()
    jd_df = jd.job_data
    assert (jd_df.iloc[0]['skills'].sort() ==
            ['c++', 'sql', 'java', 'react', 'python', 'spark'].sort())
