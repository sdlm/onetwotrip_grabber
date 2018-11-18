import aiohttp
import asyncio
from aiohttp_socks import SocksConnector

from proxy_grabber import load_from_file

PYTHON_URL = 'http://python.org'
DEFAULT_TIMEOUT = 10


async def fetch(session, **kwargs):
    async with session.get(**kwargs) as response:
        return await response.text()


async def main():
    futures = [
        load_content(url=PYTHON_URL)
    ]

    pool = load_from_file()
    for proxy in pool:
        futures.append(
            load_content(
                url=PYTHON_URL,
                proxy_address=f"{proxy['ip']}:{proxy['port']}"
            )
        )

    results = await asyncio.gather(*futures)

    count = 0
    for result in results:
        proxy = result['proxy']
        if proxy is None:
            continue

        if result['response'] is not None and proxy is not None:
            count += 1
            print(f'Valid proxy: {proxy}')

    if count == 0:
        print('No one valid proxy!')

        # if text != sample:
        #     print(f'Bad proxy: {address}')
        #     continue
        #
        # print(f'Valid proxy: {address}')


async def load_content(
        url: str,
        proxy_address: str = None,
        timeout: int = None):

    timeout_ = DEFAULT_TIMEOUT if not timeout else timeout

    if proxy_address is None:
        async with aiohttp.ClientSession() as session:
            return {
                'response': await fetch(session, url=url),
                'proxy': proxy_address
            }

    session = aiohttp.ClientSession(
        connector=SocksConnector.from_url(f'socks5://{proxy_address}'),
        timeout=aiohttp.ClientTimeout(total=timeout_)
    )
    try:
        async with session as session:
            return {
                'response': await fetch(session, url=url),
                'proxy': proxy_address
            }
    except Exception:
        print(f'Bad proxy: {proxy_address}')
        return {
            'response': None,
            'proxy': proxy_address
        }


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
