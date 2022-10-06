from flask import Flask, render_template, request, flash, redirect, url_for
# from scraper import scrape_data
# from src.models import add
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/job_analyzer"
mongodb_client = PyMongo(app)


# def add(job_title, job_location, distance):
#     # job_title="Software Engineer",
#     # job_location="Raleigh",
#     # distance=20,

#     job_df = scrape_df(job_title, job_location, distance).set_index('Job Title')

#     db.jobs.insert_many(job_df.to_dict('records'))
#     # db.job.insert_one({ 'item': "card", 'qty': 15 })

#     data = db.jobs.find()
#     for d in data:
#         print('*')
#         print(d)

#     return job_df

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        distance = request.form['distance']
        if not title:
            flash('Title is required!')
        else:
            # job_df = add(title, location, distance)
            job_df = scrape_data(title, location, distance).set_index('Job Title')
            return render_template('job_posting.html',
                                tables=[job_df.to_html(classes='data')],
                                # header="true",
                                titles=job_df.columns.values)
    return render_template('get_job_postings.html')
