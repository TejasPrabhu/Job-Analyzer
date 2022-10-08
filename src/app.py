from flask import Flask, render_template, request, flash
# from .database import read_from_db
from flask_pymongo import PyMongo
from pandas import DataFrame
import re
import numpy as np

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/job_analyzer"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        if not title:
            flash('Title is required!')
        else:
            job_df = read_from_db(request, db)
            job_df = job_df.drop('Job Description', axis=1)
            job_df = job_df.drop('_id', axis=1)
            job_df = job_df.drop('Industries', axis=1)
            job_df = job_df.drop('Job function', axis=1)
            job_df = job_df.drop('Total Applicants', axis=1)
            job_df['Job Link'] = '<a href=' + job_df['Job Link'] + '><div>' + " Apply " + '</div></a>'
            job_link = job_df.pop("Job Link")
            job_df.insert(7, "Job Link", job_link)
            job_df['Job Link'] = job_df['Job Link'].fillna('----')
            job_df['skills'] = [','.join(map(str, l)) for l in job_df['skills']]
            job_df['skills'] = job_df['skills'].replace(r'^\s*$', np.nan, regex=True)
            job_df['skills'] = job_df['skills'].fillna('----')

            return render_template('job_posting.html',
                                tables=['''
        <style>
            .table-class {border-collapse: collapse;    margin: 24px 0;    font-size: 1em;    font-family: sans-serif;    min-width: 500px;    box-shadow: 0 0 19px rgba(0, 0, 0, 0.16);}
            .table-class thead tr {background-color: #009878;    color: #ffffff;    text-align: left;}
            .table-class th,.table-class td {    text-align:center; padding: 12.4px 15.2px;}
            .table-class tbody tr {border-bottom: 1.1px solid #dddddd;}
            .table-class tbody tr:nth-of-type(even) {    background-color: #f3f3f3;}
            .table-class tbody tr:last-of-type {    border-bottom: 2.1px solid #009878;}
            .table-class tbody tr.active-row {  font-weight: bold;    color: #009878;} 
            table tr th { text-align:center; }
       </style>
        ''' +job_df.to_html(classes="table-class",render_links=True, escape=False)],
                                titles=job_df.columns.values)
    return render_template('get_job_postings.html')

def add(db, job_data):
    db.jobs.insert_many(job_data.to_dict('records'))

def read_from_db(request, db):
        title = request.form['title']
        location = request.form['location']
        distance = request.form['distance']
        rgx = re.compile('.*' + title +'.*', re.IGNORECASE)  
        data = db.jobs.find({'Job Title': rgx})
        return DataFrame(list(data))
