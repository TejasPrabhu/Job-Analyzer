from src.app import app
from src.User.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/logout')
def signout():
    return User().logout()


@app.route('/user/login', methods=['POST'])
def loginUser():
    return User().login()


@app.route('/user/profile', methods=['GET'])
def showUserProfile():
    return User().showProfile()


@app.route('/user/saveResume', methods=['POST'])
def saveResume():
    return User().saveResume()


@app.route('/healthcheck', methods=['GET'])
def healthCheck():
    return "Flask is up and running"
