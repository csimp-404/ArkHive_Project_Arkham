from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import requests
import os

#region App Setup
app = Flask(__name__)
app.config['DEBUG'] = True
bcrypt = Bcrypt(app)
app.secret_key = os.urandom(20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./backend/Arkham.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

FASTAPI_URL = "http://127.0.0.1:8000"

@app.route('/')
def login():
    response = requests.get(f"{FASTAPI_URL}/users")
    users = response.json()
    return render_template('login.html', users=users)

@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/register')
# def register():

@app.route('/message')
def messages():
    return render_template('messages.html')

if __name__ == "__main__":
    app.run(debug=True)