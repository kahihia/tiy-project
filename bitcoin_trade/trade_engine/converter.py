import io
import matplotlib.pyplot as plt
import seaborn
from base64 import b64encode


def scatter_to_base64(df, action):
    if action == "plot_current_price":
        df = df.set_index('server_time')
        x = df.index
        y = df['last']
        plt.xlabel("Time")
        plt.ylabel("Dollars Per Coin")
        plt.title("BTC-E Price")
        image = plt.plot(x, y)
        plt.setp(image, color='r', linewidth=2.0)
    if action == "plot_high":
        df = df.set_index('server_time')
        x = df.index
        y = df['high']
        plt.xlabel("Time")
        plt.ylabel("Dollars Per Coin")
        plt.title("BTC-E Price High")
        image = plt.plot(x, y)
        plt.setp(image, color='y', linewidth=2.0)
    if action == "plot_low":
        df = df.set_index('server_time')
        x = df.index
        y = df['low']
        plt.xlabel("Time")
        plt.ylabel("Dollars Per Coin")
        plt.title("BTC-E Price Low")
        image = plt.plot(x, y)
        plt.setp(image, color='g', linewidth=2.0)
    if action == "plot_avg":
        df = df.set_index('server_time')
        x = df.index
        y = df['avg']
        plt.xlabel("Time")
        plt.ylabel("Dollars Per Coin")
        plt.title("BTC-E Price Average")
        image = plt.plot(x, y)
        plt.setp(image, color='b', linewidth=2.0)
    if action == "plot_vol":
        df = df.set_index('server_time')
        x = df.index
        y = df['vol_cur']
        plt.xlabel("Time")
        plt.ylabel("Volume in Bitcoin")
        plt.title("BTC-E Volume")
        image = plt.plot(x, y)
        plt.setp(image, color='b', linewidth=2.0)
    if action == "plot_asks":
        x = df['x']
        y = df['y']
        plt.xlabel("Dollars Per Coin")
        plt.ylabel("Number of Coins")
        plt.title("Current BTC-E Ask Orders")
        image = plt.scatter(x, y)
    if action == "plot_bids":
        x = df['x']
        y = df['y']
        plt.xlabel("Dollars Per Coin")
        plt.ylabel("Number of Coins")
        plt.title("Current BTC-E Bid Orders")
        image = plt.scatter(x, y)
    image_file = io.BytesIO()
    plt.savefig(image_file, format="png")
    image_file.seek(0)
    plt.clf()
    return "data:image/png;base64, " + b64encode(image_file.read()).decode('utf-8')