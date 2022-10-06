from flask import Flask, render_template, request, flash, redirect, url_for
from .scraper import scrape_df
import pandas as pd
app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv("linkedin_scraper.csv")
    return render_template('index.html',tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        title = request.form['title']
        location = request.form['location']
        distance = request.form['distance']
        if not title:
            flash('Title is required!')
        else:
            job_df = scrape_df(title, location, distance)
            print(job_df)
            return redirect(url_for('index'))
    return render_template('get_job_postings.html')
