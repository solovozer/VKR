from market.price_models import *
from config import TICK_INTERVAL, SIMULATION_DURATION, WINDOW_SIZE
from context import SimulationContext

class Market():
    def __init__(self, price_model : BasePriceModel):
        self.model = price_model

    def step(self, context: SimulationContext):
        price = self.model.price(context)
        context.price = price
        return price

    def swap_model(self, price_model2 : BasePriceModel):
        self.model = price_model2