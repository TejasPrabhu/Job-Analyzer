import pandas as pd
from scraper import jd

skills = ['python', 'c','r', 'c++','java','hadoop','scala','flask','pandas','spark','scikit-learn',
        'numpy','php','sql','mysql','css','mongdb','nltk','fastai' , 'keras', 'pytorch','tensorflow',
        'linux','Ruby','JavaScript','django','react','reactjs','ai','ui','tableau']

skill_list = list()

jd = jd.job_data

print(jd)

def extract_skill():
    for row in jd['Job Description']:
        desc = row.lower()
        desc = [word.strip(',') for word in desc.split()]
        common_list = list(set(desc) & set(skills))
        print(common_list)
        skill_list.append(common_list)

    jd['skills'] = skill_list
    return jd

jd = extract_skill()
jd.to_csv(r'data\linkedin_scraper.csv')