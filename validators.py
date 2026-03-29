def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

def validate_qty(qty):
    if qty <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(price, order_type):
    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")