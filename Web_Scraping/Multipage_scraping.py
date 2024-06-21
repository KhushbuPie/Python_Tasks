import aiohttp
import asyncio
import time

async def fetch_page(session,url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
       "https://www.scrapingcourse.com/ecommerce", 
        "https://www.scrapingcourse.com/ecommerce/page/2/", 
        "https://www.scrapingcourse.com/ecommerce/page/3/" 
    ]

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []

        for url in urls:
            tasks.append(fetch_page(session,url))

        htmls = await asyncio.gather(*tasks)

    end_time = time.time()

    for url, html in zip(urls, htmls):
        print(f"Content from {url}:\n{html}\n")

    print(f"Time taken: {end_time - start_time} seconds")
    
asyncio.run(main())




