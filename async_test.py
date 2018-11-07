import aiohttp
import asyncio
from aiohttp_socks import SocksConnector

from proxy_grabber import load_from_file

PYTHON_URL = 'http://python.org'


async def fetch(session, **kwargs):
    async with session.get(**kwargs) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        sample = await fetch(session, url=PYTHON_URL)

    timeout = aiohttp.ClientTimeout(total=3)
    pool = load_from_file()
    for proxy in pool:
        address = f"{proxy['ip']}:{proxy['port']}"

        connector = SocksConnector.from_url(f'socks5://{address}')
        try:
            async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
                text = await fetch(session, url=PYTHON_URL)
        except Exception:
            print(f'Bad proxy: {address}')
            continue

        if text != sample:
            print(f'Bad proxy: {address}')
            continue

        print(f'Valid proxy: {address}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
