import aiohttp
import asyncio
from aiohttp_socks import SocksConnector

from proxy_grabber import load_from_file, save_to_file

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

    results = await asyncio.gather(*futures, return_exceptions=True)

    renew_pool = []
    for result in results:
        if isinstance(result, Exception):
            continue

        proxy = result['proxy']
        if proxy is None:
            continue

        if result['response'] is not None and proxy is not None:
            print(f'Valid proxy: {proxy}')
            proxy_obj = {
                'ip': proxy.split(':')[0],
                'port': proxy.split(':')[1],
            }
            renew_pool.append(proxy_obj)

    if not renew_pool:
        print('No one valid proxy!')

    save_to_file(renew_pool)


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
