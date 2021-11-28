import asyncio
from binance import AsyncClient, BinanceSocketManager


async def binance_ws_client():
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.symbol_book_ticker_socket("BTCUSDT")

    async with ts as tscm:
        while True:
            res = await tscm.recv()
            print(res)


asyncio.run(binance_ws_client())