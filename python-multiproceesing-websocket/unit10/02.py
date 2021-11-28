import websockets
import asyncio 
import json
import pprint

async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()

        subscribe_fmt = {
            "type": "ticker",
            "symbols": ["BTC_KRW"],
            "tickTypes": ["24H"]
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            rdata = await websocket.recv()
            data = json.loads(rdata)
            pprint.pprint(data)

asyncio.run(bithumb_ws_client())