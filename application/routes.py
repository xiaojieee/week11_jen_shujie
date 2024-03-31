from flask import render_template, url_for, request, redirect, session
from application import app
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Pa$$w0rd",  # blank for mac
  database="tea_db"
)

cursor = mydb.cursor()


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', active_home='active')


@app.route('/about/')
def about():
    return render_template('about.html', active_about='active')


tea_list = {'Strawberry': 'images/strawberry.webp', 'Brown Sugar': 'images/bsugar.jpg',
            'Taro': 'images/strawberry.webp', 'Matcha': 'images/strawberry.webp', 'Rose Milk':
                'images/strawberry.webp', 'Mango Boba': 'images/strawberry.webp',
            'Classic Milk': 'images/strawberry.webp', 'Honey Dew': 'images/strawberry.webp'}


@app.route('/order/')
def order():
    return render_template('order.html', active_order='active', tea_list=tea_list)


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

        # Insert data into the tea_orders table
        sql = "INSERT INTO tea_orders (name_n, tea_type) VALUES (%s, %s)"
        values = (name, teaType)

        cursor.execute(sql, values)
        mydb.commit()

        return redirect(url_for('complete'))

    return render_template('basket.html')


@app.route('/complete/')
def complete():
    return render_template('complete_order.html')
