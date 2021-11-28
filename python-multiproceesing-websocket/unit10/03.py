import websockets
import asyncio 
import json
import pprint

async def upbit_ws_client():
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri, ping_interval=60) as websocket:
        subscribe_fmt = [
            {"ticket": "test"},
            {"type": "ticker", "codes": ["KRW-BTC"], "isOnlyRealtime": True},
            {"format": "DEFAULT"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            rdata = await websocket.recv()
            data = json.loads(rdata)
            pprint.pprint(data)

asyncio.run(upbit_ws_client())