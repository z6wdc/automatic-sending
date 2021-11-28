import re
import time
import aiohttp
import asyncio
import multiprocessing as mp
from bs4 import BeautifulSoup
from urllib.request import urljoin

INTERVAL = 15

seen = set()
unseen = set(range(1, 61))

async def crawl(index):
    url = f'https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88&limit={INTERVAL}&start={index*INTERVAL}'
    res = requests.get(url)
    return res

