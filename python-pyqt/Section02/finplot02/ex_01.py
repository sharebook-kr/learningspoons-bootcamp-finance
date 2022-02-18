import math
import pandas as pd
import finplot as fplt
import requests
import time

def update():
    # load data
    limit = 500
    start = int(time.time()*1000) - (500-2)*60*1000
    url = 'https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist?limit=%i&sort=1&start=%i' % (limit, start)
    table = requests.get(url).json()
    df = pd.DataFrame(table, columns='time open close high low volume'.split())

    # calculate indicator
    # pick columns for our three data sources: candlesticks and TD sequencial labels for up/down
    candlesticks = df['time open close high low'.split()]
    if not plots:
        # first time we create the plots
        global ax
        plots.append(fplt.candlestick_ochl(candlesticks))
    else:
        # every time after we just update the data sources on each plot
        plots[0].update_data(candlesticks)


plots = []
ax = fplt.create_plot('Realtime Bitcoin/Dollar 1m TD Sequential (BitFinex REST)', init_zoom_periods=100, maximize=False)
update()
fplt.timer_callback(update, 5.0) # update (using synchronous rest call) every N seconds

fplt.show()