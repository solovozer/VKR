"""OHLCV data structures and price database."""
import pandas as pd


class OHLCV:
    def __init__(
        self,
        time,
        volume=1,
        price=None,
        open=None,
        high=None,
        low=None,
        close=None
    ):
        self.time = time
        self.open = price if open is None else open
        self.high = price if high is None else high
        self.low = price if low is None else low
        self.close = price if close is None else close
        self.volume = volume


class Price_DB:
    def __init__(self):
        self.prices = []

    def save(self, price: OHLCV):
        self.prices.append(price)

    def get_recent(self, count):
        return self.prices[-count:]

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame({
            "Open":   [x.open for x in self.prices],
            "High":   [x.high for x in self.prices],
            "Low":    [x.low for x in self.prices],
            "Close":  [x.close for x in self.prices],
            "Volume": [x.volume for x in self.prices],
        }, index=[x.time for x in self.prices])

    def to_df_recent(self, count) -> pd.DataFrame:
        recent = self.prices[-count:]
        return pd.DataFrame({
            "Open":   [x.open for x in recent],
            "High":   [x.high for x in recent],
            "Low":    [x.low for x in recent],
            "Close":  [x.close for x in recent],
            "Volume": [x.volume for x in recent],
        }, index=[x.time for x in recent])
