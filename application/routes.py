from flask import render_template, url_for, request, redirect, session
from application import app
from application.basket import add_to_basket
from application.data_access import get_tea


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html', active_home='active')


@app.route('/about/')
def about():
    return render_template('about.html', active_about='active')


@app.route('/order/', methods=['GET', 'POST'])
def order():
    tea_from_db = get_tea()

    if request.method == 'POST':

        if 'basket' not in session:
            session['basket'] = []

        tea_ids = request.form.getlist('tea_id[]')
        tea_names = request.form.getlist('tea_name[]')
        tea_prices = request.form.getlist('tea_price[]')
        quantities = request.form.getlist('quantity[]')
        filenames = request.form.getlist('tea_filename[]')

        tea_chosen = zip(tea_ids, tea_names, tea_prices, quantities, filenames
        add_to_basket(tea_chosen, session['basket'])

    return render_template('order.html', active_order='active', tea_db=tea_from_db)


@app.route('/stores/')
def our_stores():
    return render_template('store.html', active_stores='active')


@app.route('/basket/')
def basket():
    customer_basket = session.get('basket', [])  # Get basket from session, return empty list if not present
    return render_template('basketcopy.html', basket=customer_basket)


# @app.route('/basket/', methods=['GET', 'POST'])
# def basket():
#
#     if request.method == 'POST':
#         name = request.form['name']
#         teaType = request.form['teaType']
#
#         submit_order_db(name, teaType)
#
#         return redirect(url_for('complete'))
#
#     return render_template('basket.html')


@app.route('/complete/')
def complete():
    return render_template('complete_order.html')
