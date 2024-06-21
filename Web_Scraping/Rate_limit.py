import asyncio
import logging
import re
import sys
import urllib.error
import urllib.parse
from typing import IO, Set

import aiofiles
import aiohttp
from aiohttp import ClientSession
from aiolimiter import AsyncLimiter

import mysql.connector

#set up basic configuration for logging system
logging.basicConfig(  
    format="%(asctime)s %(levelname)s:%(message)s",#specifies the format of the log messages
    level=logging.DEBUG, 
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("charsetprober").disabled = True

HREF_RE = re.compile(r'href="(.*?)"')

rate_limiter = AsyncLimiter(max_rate=5, time_period=1)

async def fetch_html(url:str, session:ClientSession, **kwargs) -> str:
    """GET request wrapper to fetch page HTML."""
    async with rate_limiter:
        async with session.get(url, **kwargs) as resp:
            resp.raise_for_status()
            logger.info("Got response [%s] for URL: %s", resp.status, url)
            html = await resp.text()
            return html

async def parse(url: str, session: ClientSession, **kwargs) -> Set[str]:
    """Fetch and parse HTML to extract links."""
    found = set()
    try:
        html = await fetch_html(url=url, session=session, **kwargs)
    except (aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as e:
        logger.error("aiohttp exception for %s [%s]: %s", url, getattr(e,"status", None),getattr(e,"message", None))
        return found
    except Exception as e:
        logger.exception("Non-aiohttp exception occurred: %s", getattr(e,"__dict__", {}))
        return found
    else:
        for link in HREF_RE.findall(html):
            try: 
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError):
                logger.exception("Error parsing URL: %s", link)
                pass
            else:
                found.add(abslink)
        logger.info("Found %d links for %s", len(found), url)
        return found

async def write_one(file: IO, url:str, **kwargs) -> None:
    """ Fetch , parse, and write for one URL."""
    res= await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("wrote results for source URL: %s", url)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Digipie",
        )

        cursor = connection.cursor()

        for p in res:
            sql ="Insert Into scraped_data (source_url, parsed_url) VALUES (%s,%s)"
            val =(url, p)
            cursor.execute(sql,val)

        connection.commit()
        logger.info("Inserted data successfully")

    except Exception as e:
        logger.error("Error in insert data:%s", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            logger.info("Mysql connection closed")


async def bulk_crawl_and_write(file: IO, urls:Set[str], **kwargs)-> None:
    """Crawl multiple URLs and write results."""
    async with ClientSession() as session:
        tasks = [write_one(file=file, url=url, session=session, **kwargs) for url in urls]
        await asyncio.gather(*tasks)
        # tasks = []
        # for url in urls:
        #     tasks.append(write_one(file=file, url=url, session=session, **kwargs))
        #     await asyncio.gather(*tasks)

if __name__ == "__main__":
    import pathlib

    assert sys.version_info >= (3,7), "Script requies Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tparsed_url\n")

    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))

    