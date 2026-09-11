from typing import Tuple
from .orders import Order
from API import API

class OrderExecutor:
    def execute(self, order: Order):
        if order.quantity < 0: API.Sell(order)
        if order.quantity > 0: API.Buy(order) 
