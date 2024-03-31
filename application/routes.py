from flask import render_template, url_for, request, redirect, session
from application import app
from application.data_access import get_tea, submit_order_db


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', active_home='active')


@app.route('/about/')
def about():
    return render_template('about.html', active_about='active')


@app.route('/order/')
def order():
    tea_from_db = get_tea()
    return render_template('order.html', active_order='active', tea_db=tea_from_db)


@app.route('/stores/')
def our_stores():
    return render_template('store.html', active_stores='active')


# @app.route('/basket/')
# def basket():
#     return render_template('basket.html')


@app.route('/basket/', methods=['GET', 'POST'])
def basket():

    if request.method == 'POST':
        name = request.form['name']
        teaType = request.form['teaType']

        submit_order_db(name, teaType)

        return redirect(url_for('complete'))

    return render_template('basket.html')


@app.route('/complete/')
def complete():
    return render_template('complete_order.html')
