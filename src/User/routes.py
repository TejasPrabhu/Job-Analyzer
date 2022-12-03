import sys
# sys.path.append('../src')
from src.app import app
from flask import Flask, render_template
from src.User.models import User


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()


@app.route('/user/logout')
def signout():
    return User().logout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/user/profile', methods=['GET'])
def showUserProfile():
    return User().showProfile()
