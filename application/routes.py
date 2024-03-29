from flask import render_template, url_for, request, redirect, session

from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#
# @app.route('/about')
# def about():
#
#
# @app.route('/order')
# def order():
#
#
# @app.route('/stores')
# def our_stores():