from flask import render_template, url_for, request, redirect, session
from application import app
from application.basket_functions import add_to_basket, calculate_totals
from application.data_access import get_tea, submit_order_db, submit_collection_db, get_last_collection_id
from application.order_functions import create_collection_time


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

        tea_chosen = zip(tea_ids, tea_names, tea_prices, quantities, filenames)
        add_to_basket(tea_chosen, session['basket'])

    return render_template('order.html', active_order='active', tea_db=tea_from_db)


@app.route('/stores/')
def our_stores():
    return render_template('store.html', active_stores='active')


@app.route('/basket/', methods=['GET', 'POST'])
def basket():

    customer_basket = session.get('basket', [])  # Get basket from session, return empty list if not present

    if customer_basket and request.method == 'POST':
        customer_name = request.form['customer_name']

        collection_time = create_collection_time()
        submit_collection_db(collection_time)

        for item in customer_basket:
            tea_id = int(item['tea_id'])
            quantity_str = item.get('quantity', '')
            try:
                quantity = int(quantity_str)
            except ValueError:
                continue

            submit_order_db(tea_id, quantity, customer_name)

        # Removing/ending the basket session
        session.pop('basket')
        return redirect(url_for('complete'))

    total_price, total_quantity = calculate_totals(customer_basket)
    return render_template('basketcopy.html', basket=customer_basket, total_price=total_price, total_quantity=total_quantity)


@app.route('/basket/clear')
def clear_basket():
    session.pop('basket')
    return redirect(url_for('basket'))  # Redirect back to the basket page


@app.route('/complete/')
def complete():
    collection_number = get_last_collection_id()
    return render_template('complete_order.html', collection_number=collection_number)


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
