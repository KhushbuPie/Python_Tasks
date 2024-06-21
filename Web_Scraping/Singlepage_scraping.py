# #Client Example
# import aiohttp
# import asyncio

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:
#             print("Status:",response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")
# asyncio.run(main())

# #Server example:

# from aiohttp import web

# async def handle(request):
#     name = request.match_info.get('name',"Anonymous")
#     text = "Hello, "+name
#     return web.Response(text=text)

# app = web.Application()
# app.add_routes([web.get('/', handle),web.get('/{name}',handle)])

# if __name__=="__main__":
#     web.run_app(app)

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




