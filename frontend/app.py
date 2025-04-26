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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Call the API to retrieve the user by username
        try:
            response = requests.get(f"{FASTAPI_URL}/users/{username}")
            user = response.json() if response.status_code == 200 else None
        except requests.exceptions.RequestException as e:
            return f"Error connecting to the user API: {str(e)}"
        
        if user:
            # Compare the provided password with the stored hashed password
            if bcrypt.check_password_hash(password.encode('utf-8'), user['password'].encode('utf-8')):
                return redirect(url_for('home'))
            else:
                error_message = 'Invalid password, please try again.'
                return error_message
        else:
            error_message = 'User not found, please try again.'
            return error_message
        
    return render_template('login.html')

@app.route('/home')
def home():
#    return render_template('home.html')
    response = requests.get(f"{FASTAPI_URL}/username")
    username = response.json() if response.status_code == 200 else "Guest"
    response = requests.get(f"{FASTAPI_URL}/messages/received/{1}")
    received_messages = response.json() if response.status_code == 200 else []
    response = requests.get(f"{FASTAPI_URL}/messages/recent/{1}")
    recent_messages = response.json() if response.status_code == 200 else []
    response = requests.get(f"{FASTAPI_URL}/users")
    users = response.json() if response.status_code == 200 else []
    return render_template(
        'home.html',
        username=username,
        received_messages=received_messages,
        recent_messages=recent_messages,
        users=users
    )

# @app.route('/register')
# def register():

@app.route('/message')
def messages():
    return render_template('messages.html')

if __name__ == "__main__":
    app.run(debug=True)