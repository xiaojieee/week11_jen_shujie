def add_to_basket(zipped_teas, session):

    for tea_id, tea_name, tea_price, quantity, filename in zipped_teas:

        session.append({'tea_id': tea_id, 'tea_name': tea_name, 'tea_price': tea_price, 'quantity':
            quantity, 'tea_filename': filename})