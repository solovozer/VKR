from trading.orders import Order

class API():
    def Sell(order: Order):
        print(f"Time {order.time}: Sold {order.quantity} at {order.price}")
    def Buy(order:Order):
        print(f"Time {order.time}: Bought {order.quantity} at {order.price}")