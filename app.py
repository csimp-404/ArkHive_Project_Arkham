from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests
import os

#region App Setup
app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = os.urandom(20)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./backend/Arkham.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

FASTAPI_URL = "http://127.0.0.1:8000"

# @app.route('/')
# def login(username):
#     response = requests.get(f"{FASTAPI_URL}/users")
#     user = response.json()
#     return
# @app.route('/home')
# def home():

# @app.route('/register')
# def register():

# @app.route('message')
# def messages():



# if __name__ == "__main__":
#     app.run(debug=True)