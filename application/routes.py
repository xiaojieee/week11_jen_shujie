from flask import render_template, url_for, request, redirect, session

from application import app


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', active_home='active')


@app.route('/about/')
def about():
    return render_template('about.html', active_about='active')


tea_list = {'Strawberry': 'images/strawberry.webp', 'Brown Sugar': 'images/strawberry.webp',
            'Taro': 'images/strawberry.webp', 'Matcha': 'images/strawberry.webp', 'Rose Milk':
                'images/strawberry.webp', 'Mango Boba': 'images/strawberry.webp',
            'Classic Milk': 'images/strawberry.webp', 'Honey Dew': 'images/strawberry.webp'}


@app.route('/order/')
def order():
    return render_template('order.html', active_order='active', tea_list=tea_list)


@app.route('/stores/')
def our_stores():
    return render_template('store.html', active_stores='active')

@app.route('/basket/')
def basket():
    return render_template('basket.html', active_basket='active')
