#Asynchronous webscraping

import aiohttp
import asyncio
import time

async def main():
    url= "https://www.scrapingcourse.com/ecommerce/"

    start_time = time.time()

    content = await fetch(url)

    print(content)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

asyncio.run(main())




