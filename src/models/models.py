from torch import nn
from context import SimulationContext

class BaseModel():
    def __init__(self):
        pass

    def decide(self, context: SimulationContext): 
        return 1.0

class RudimentaryAlgorithm(BaseModel):
    def __init__(self):
        pass

    def decide(self, context: SimulationContext):
        if (context.time & 1) == 0: return 1.0
        else: return 0.0