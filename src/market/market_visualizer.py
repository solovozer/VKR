import matplotlib.pyplot as plt


class MarketVisualizer:
    def __init__(self):
        plt.ion()

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])

        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Price")
        self.ax.set_title("Simulated Market")

    def draw(self, recent):
        self.line.set_data(recent.index, recent["Close"])

        self.ax.relim()
        self.ax.autoscale_view()

        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()

    def pause(self, tick_interval):
        plt.pause(tick_interval)

    def show_price(self, t, price):
        print(f"Price at time={t}: {price}")