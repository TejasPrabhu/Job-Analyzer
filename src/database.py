# from .app import mongodb_client

# db = mongodb_client.db

# def add(db, job_data):
#     # job_df = scrape_df(job_title, job_location, distance).set_index('Job Title')
#     db.jobs.insert_many(job_data.to_dict('records'))
#     # db.job.insert_one({ 'item': "card", 'qty': 15 })


# def read_from_db(request, db):
#         title = request.form['title']
#         location = request.form['location']
#         distance = request.form['distance']

#         return db.jobs.find({ "Location": location, "Job Title": title})







