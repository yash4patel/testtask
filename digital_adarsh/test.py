import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"{name} finished")

async def main():
    # Sequential execution (not concurrent)
    p1 =task("A", 2)
    p2 = task("B", 1)  # Starts after A finishes

    # a=await p1
    # b=await p2
    await asyncio.gather(p1,p2)

asyncio.run(main())
