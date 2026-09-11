from simulator.simulator import Simulator
from market.market import *
from market.market_visualizer import *
from models import *
from market.data import Price_DB
from trading.executor import OrderExecutor
from config import WINDOW_SIZE, SIMULATION_DURATION


market = Market(BasePriceModel())
visualizer = MarketVisualizer()
price_db = Price_DB()
orderExecutor = OrderExecutor()

sim = Simulator(market= market,
                visualizer= visualizer,
                price_db= price_db,
                executor = orderExecutor,
                )
if __name__ == "__main__":
    sim.run_simulation()