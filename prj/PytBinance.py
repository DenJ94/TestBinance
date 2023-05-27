# запустить код в терминале
# pip install python-binance

from binance.client import Client
from binance.exceptions import BinanceAPIException
import random

def create_orders(data):
    client = Client('YOUR_API_KEY', 'YOUR_SECRET_KEY')

    volume_per_order = data["volume"] / data["number"]
    orders = []

    for i in range(data["number"]):
        order_volume = random.uniform(volume_per_order - data["amountDif"], 
                                      volume_per_order + data["amountDif"])
        order_price = random.uniform(data["priceMin"], data["priceMax"])

        # расчёт количества Btc, которое можно купить на рассчитанный объем в Usd
        # округление до 6 десятичных знаков
        quantity = round(order_volume / order_price, 6)

        try:
            order = client.order_limit(
                symbol='BTCUSDT',
                side=data["side"],
                quantity=quantity,
                price=order_price
            )
        except BinanceAPIException as e:
            print(f"Error when creating order: {e}")
            continue

        orders.append(order)

    return orders