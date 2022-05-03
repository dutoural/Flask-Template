from app import app
from app.config import config
from flask import url_for, render_template,request,jsonify

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

