# Start with the idea of a stock
# Stock is a dictionary
# name, symbol, price, quantity

def create_stock(name, symbol, price, quantity):
    _d = {}

    _d['name'] = name
    _d['symbol'] = symbol
    _d['price'] = price
    _d['quantity'] = quantity
    _d['investment'] = price * quantity

    return _d