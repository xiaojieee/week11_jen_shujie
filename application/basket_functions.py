def add_to_basket(zipped_teas, session):

    for tea_id, tea_name, tea_price, quantity, filename in zipped_teas:

        if quantity:
            session.append({'tea_id': tea_id,
                            'tea_name': tea_name,
                            'tea_price': float(tea_price),
                            'quantity': quantity,
                            'tea_filename': filename})


def calculate_totals(basket):
    total_price = 0
    total_quantity = 0

    for tea in basket:
        try:
            tea_price = float(tea['tea_price'])
            quantity_str = tea.get('quantity', '')
            if quantity_str:
                quantity = int(quantity_str)
                total_price += tea_price * quantity
                total_quantity += quantity
        except (ValueError, TypeError):
            continue

    total_price_rounded = "{:.2f}".format(total_price)

    return total_price_rounded, total_quantity
