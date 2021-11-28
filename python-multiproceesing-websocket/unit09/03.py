import asyncio 
import time

async def make_americano():
    print("americano start", time.strftime('%X'))
    await asyncio.sleep(3)
    print("americano end", time.strftime('%X'))

async def make_latte():
    print("latte start", time.strftime('%X'))
    await asyncio.sleep(5)
    print("latte end", time.strftime('%X'))

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    await asyncio.gather(
        coro1, 
        coro2
    )

asyncio.run(main())