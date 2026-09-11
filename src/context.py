from dataclasses import dataclass


@dataclass
class SimulationContext:
    time: int 
    price: float = None 
    previous_price: float = None
