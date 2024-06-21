# Task : Generating Random Numbers with Asynchronous Functions
import asyncio
import random

async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(f"makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(f"---> Finished: makerandom({idx}) == {i}")
    return i

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")



# Task : Chaining Coroutines to Perform Sequential Tasks
import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2({n}, {arg}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2({n}, {arg}) == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"--> Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))

if __name__ == "__main__":
    import sys
    random.seed(444)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")


# Task : Understanding Generators and Async Generators
from itertools import cycle

def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))

e = endless()
total = 0
for i in e:
    if total < 30:
        print(i, end=" ")
        total += i
    else:
        print()
        break

async def mygen(u: int = 10):
    """Yield power of 2."""
    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        await asyncio.sleep(0.1)

async def main():
    g = [i async for i in mygen()]
    f = [j async for j in mygen() if not (j // 3 % 5)]
    return g, f

g, f = asyncio.run(main())
print("g:", g, "\nf:", f)


# Task : Fetching Data Concurrently Using aiohttp
import asyncio
import aiohttp
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def fetch(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raise an exception for HTTP errors
            html = await response.text()
            logger.info(f"Successfully fetched {url}")
            return html
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(url, session)) for url in urls]
        
        for task in tasks:
            task.add_done_callback(log_result)
        
        responses = await asyncio.gather(*tasks)
        
        # Further processing of responses if needed
        for response in responses:
            if response:
                print(response[:100])  # Print the first 100 characters of each response

def log_result(task):
    try:
        result = task.result()
        if result is None:
            logger.error("Task failed.")
        else:
            logger.info("Task completed successfully.")
    except Exception as e:
        logger.error(f"Task raised an exception: {e}")

# List of URLs to fetch
urls = [
    "http://example.com",
    "http://example.org",
    "http://example.net",
    "http://invalid-url"  # Add an invalid URL to test error handling
]

# Run the main function
asyncio.run(main(urls))


