import aiohttp
import asyncio
import time
import aiomysql

async def fetch_page(session,url):
    async with session.get(url) as response:
        return await response.text()

async def save_to_databse(pool, url, html):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("Insert into scraped(url, html) values (%s,%s)", (url,html))
        await conn.commit()

async def main():
    urls = [
        "https://www.scrapingcourse.com/ecommerce",
        "https://www.scrapingcourse.com/ecommerce/page/2/",
        "https://www.scrapingcourse.com/ecommerce/page/3/"
    ]
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        rate_limiter = asyncio.Semaphore(5)

        async with aiomysql.create_pool(host="localhost", port=3306,user="root",password="",db="Digipie") as pool:

            for url in urls:
                async with rate_limiter:
                    tasks.append(fetch_page(session, url))

            htmls = await asyncio.gather(*tasks)

            save_tasks = [save_to_databse(pool, url, html) for url, html in zip(urls, htmls)]
            await asyncio.gather(*save_tasks)

    end_time= time.time()

    for url, html in zip(urls,htmls):
        with open(f"{url.replace('/','_').strip('_')}.html","w", encoding="utf-8") as f:
            f.write(html)
        print(f"Content from {url} sabved.")
    print(f"Time taken: {end_time-start_time} seconds")

asyncio.run(main())