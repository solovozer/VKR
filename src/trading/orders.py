class Order:
    def __init__(self, time, quantity: float, price: float):
        self.time = time
        self.quantity = quantity
        self.price = price

    def __repr__(self) -> str:
        return (
            f"Order time: {self.time}, "
            f"Quantity: {self.quantity}"
            f"Price: {self.price}"
        )