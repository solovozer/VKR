from market import *
from trading import *
from models import *
from config import SIMULATION_DURATION, WINDOW_SIZE
from context import SimulationContext


class Simulator():
    def __init__(self, 
                market : Market,
                visualizer : MarketVisualizer,
                price_db : Price_DB,
                executor : OrderExecutor,
                model: BaseModel = BaseModel()): 
        self.market = market
        self.model = model
        self.visualizer = visualizer
        self.executor = executor
        self.price_db = price_db
        self.time = 0

    def step(self):           # = 0 -> Do nothing, < 0 -> Sell, > 0 = Buy
        context = SimulationContext(time=self.time,
)
        price = self.market.step(context)
        self.price_db.save(OHLCV(time=self.time, price=price))
        self.visualizer.draw(self.price_db.to_df_recent(count=WINDOW_SIZE))

        quantity = self.model.decide(context)
        #USE A MODEL TO DECIDE THE QUANTITY. 
        #MODEL WILL CONTAIN LOGIC FOR EXECUTION LEVEL TWO: BUY X AMOUNT IN TIME T  
        #EXECUTE LEVEL ONE: BUY X AMOUNT INSTANTLY 
        self.executor.execute(Order(time=self.time, price=price, quantity=quantity)) 
        if quantity != 0: self.price_db.save(OHLCV(time=self.time, price=price))
        self.time += 1

    def run_simulation(self, duration = SIMULATION_DURATION):
        while self.time != duration: 
            try: self.step()
            except KeyboardInterrupt: break