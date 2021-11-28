import asyncio

async def americano():
    print("americano start")
    await asyncio.sleep(3)
    print("americano end")

async def latte():
    print("latte start")
    await asyncio.sleep(3)
    print("latte end")

async def main():
    coro1 = americano()
    coro2 = latte()
    await asyncio.gather(
        coro1,
        coro2
    )

print("main start")
asyncio.run(main())
print("main end")