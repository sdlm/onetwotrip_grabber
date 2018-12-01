import os
import json
from typing import List, Optional

import requests

FILENAME = 'proxy_pool.json'


def get_proxy() -> Optional[dict]:
    response = requests.get('https://api.getproxylist.com/proxy?protocol[]=socks5')
    proxy = response.json()
    try:
        return {
            'ip': proxy['ip'],
            'port': proxy['port'],
        }
    except KeyError:
        return None


def get_proxy_pool(count: int = 1) -> List:
    proxies = [
        get_proxy() for _ in range(count)
    ]
    return [proxy for proxy in proxies if proxy]


def save_to_file(pool: List):
    with open(FILENAME, 'w') as outfile:
        json.dump(pool, outfile)


def load_from_file() -> List:
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME) as json_data:
        return json.load(json_data)


if __name__ == '__main__':
    pool = load_from_file()
    new_proxies = get_proxy_pool(10)
    pool.extend(new_proxies)
    print(f'Pool contain {len(new_proxies)} proxies.')
    save_to_file(pool)
