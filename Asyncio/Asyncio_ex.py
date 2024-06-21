import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(4, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1,'hello')
        )
        task2 = tg.create_task(
            say_after(2,'World')
        )
        print(f"started at {time.strftime('%X')}")

    print(f'finished at {time.strftime('%X')}')
asyncio.run(main())
# print(asyncio.get_running_loop())
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main())

#fetching URLs asynchronously

import asyncio
import aiohttp

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.create_task(fetch(url,session)))

        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response[:100])

urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net"
]
asyncio.run(main(urls))

