import pandas as pd
from nltk.corpus import stopwords
from textblob import Word
from textblob import TextBlob
# import nltk
# nltk.download('averaged_perceptron_tagger')
other_stop_words = ['junior', 'senior', 'experience', 'etc', 'job', 'work',
                    'company', 'technique', 'candidate', 'skill', 'skills',
                    'language', 'menu', 'inc', 'new', 'plus', 'years',
                    'technology', 'organization', 'ceo', 'cto', 'account',
                    'manager', 'product', 'revenue', 'strong', 'team',
                    'service', 'code', 'opportunity', 'time', 'customer',
                    'health', 'application', 'technical', 'engineer', 'based',
                    'environment', 'engineering', 'u', 'sa',
                    'great']
technical_skills = ['python', 'c', 'r', 'c++', 'java', 'hadoop', 'scala',
                    'flask', 'pandas', 'spark', 'scikit-learn', 'numpy', 'php',
                    'sql', 'mysql', 'css', 'mongdb', 'nltk', 'fastai', 'keras',
                    'pytorch', 'tensorflow', 'linux', 'Ruby', 'JavaScript',
                    'django', 'react', 'reactjs', 'ai', 'ui', 'tableau']


def data_preprocess(df):
    df['Job Description'] = df['Job Description'].apply(
        lambda x: " ".join(x.lower()for x in x.split()))
    df['Job Description'] = df['Job Description'] .str.replace(r'[^\w\s]', ' ')
    df['Job Description'] = df['Job Description'].str.replace(r'\d+', '')
    stop = stopwords.words('english')
    df['Job Description'] = df['Job Description'].apply(
        lambda x: " ".join(x for x in x.split() if x not in stop))
    df['Job Description'] = df['Job Description'].apply(
        lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    df['Job Description'] = df['Job Description'].apply(
        lambda x: " ".join(x for x in x.split() if x not in other_stop_words))
    return df


def get_skills(df):
    jd_string = df['Job Description'].sum()
    jd_list = jd_string.split()
    jd_freq_dict = word_list_to_freq_dict(jd_list)
    jd_sort_freq_list = sort_freq_dict(jd_freq_dict)
    skills_list = []
    technical_skills_list = []
    for idx in jd_sort_freq_list:
        if idx[0] > 8:
            skills_list.append(idx[1])
            if idx[1] in technical_skills:
                technical_skills_list.append(idx[1])

    txt = " ".join(skills_list)
    skills_list = [w for (w, pos) in TextBlob(
        txt).pos_tags if pos.startswith("JJ")][:6]
    return technical_skills_list, skills_list


def word_list_to_freq_dict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))


def sort_freq_dict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux


data_scraper = pd.read_csv("./data/linkedin_scraper.csv")

data_processed = data_preprocess(data_scraper)
skills_list_1, skills_list_2 = get_skills(data_processed)

print(skills_list_1)
print(skills_list_2)
