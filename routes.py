from flask import Flask, render_template, request, redirect, url_for, flash
from __init__ import app, db

@app.route('/')
@app.route('/home')
def home():
    
    user = {
        "first_name": "marvin",
        "last_name": "luyombya",
        "role": "administrator",
        "email": "student01@gmail.com"
    }

    return render_template('home.html', user=user)