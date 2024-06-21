import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time

async def fetch_page(session,url):
    async with session.get(url) as response:
        html_content = await response.text()
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup

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

    for url, soup in zip(urls, htmls):
        product_list = soup.find('ul', class_='products')
        products = product_list.find_all('li')

        for product in products:
            name = product.find('h2').text
            price = product.find('span', class_='amount').text
            image = product.find('img')['src']
            print(f"Product from {url}:\nName: {name}\nPrice: {price}\nImage: {image}\n")
    print(f"Time taken: {end_time-start_time} seconds")

asyncio.run(main())
