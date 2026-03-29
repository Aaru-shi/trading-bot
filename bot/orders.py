import logging
from urllib import response
from bot.rest_client import send_order

def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order {symbol} {side} {order_type}")

        response = send_order(symbol, side, order_type, quantity, price)

        logging.info(response)

        print("API RESPONSE:", response)   # 👈 ADD THIS
        return response

    except Exception as e:
        logging.error(str(e))
        raise
