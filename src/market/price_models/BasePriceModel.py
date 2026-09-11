import numpy as np
from context import SimulationContext

class BasePriceModel():
    def __init__(self):
        pass

    def price(self, context: SimulationContext):
        return context.time