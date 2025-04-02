from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import requests
import os

#region App Setup
app = Flask(__name__)
app.config['DEBUG'] = True

