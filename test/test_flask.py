from src.app import app


def test_home_page():

    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Get Job Postings" in response.data


def test_search_page():
    response = app.test_client().get('/search')
    assert response.status_code == 200
    assert b"Job Title" in response.data
    assert b"Location" in response.data
    assert b"Company Name" in response.data
    assert b"Technical skills" in response.data
    assert b"Job Type" in response.data


def test_search_page_submit():

    response = app.test_client().post("/search", data={
        "title": "Software Engineer",
        "type": "Full-Time",
        "location": "Raleigh",
        "companyName": "Amazon",
        "skills": "Python",
    })
    assert response.status_code == 200
