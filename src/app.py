from flask import Flask, render_template, request, flash
# from .database import read_from_db
from flask_pymongo import PyMongo
from pandas import DataFrame
import re

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
            return render_template('job_posting.html',
                                tables=[job_df.to_html(classes='data')],
                                # header="true",
                                titles=job_df.columns.values)
    return render_template('get_job_postings.html')


def add(db, job_data):
    # job_df = scrape_df(job_title, job_location, distance).set_index('Job Title')
    db.jobs.insert_many(job_data.to_dict('records'))
    # db.job.insert_one({ 'item': "card", 'qty': 15 })


def read_from_db(request, db):
        title = request.form['title']
        location = request.form['location']
        distance = request.form['distance']
        rgx = re.compile('.*' + title +'.*', re.IGNORECASE)  # compile the regex
        data = db.jobs.find({'Job Title': rgx})
        return DataFrame(list(data))
