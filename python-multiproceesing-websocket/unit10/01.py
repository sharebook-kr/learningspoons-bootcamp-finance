import websockets
import asyncio 


async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(greeting)

asyncio.run(bithumb_ws_client())