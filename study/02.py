import asyncio 

async def hello():
    print("hello")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()