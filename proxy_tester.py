from pprint import pprint

import requests

from proxy_grabber import load_from_file, save_to_file

GITHUB_URL = 'https://api.github.com/user'
AUTH = ('user', 'pass')


if __name__ == '__main__':
    response = requests.get(
        url=GITHUB_URL,
        auth=AUTH,
    )
    sample = response.json()

    pool = load_from_file()
    renew_pool = []
    for proxy in pool:
        address = f"{proxy['ip']}:{proxy['port']}"
        try:
            response = requests.get(
                url=GITHUB_URL,
                auth=AUTH,
                proxies={
                    'https': f"socks5://{address}"
                },
                timeout=5
            )

        except requests.exceptions.ConnectionError:
            print(f'Bad proxy: {address}, connection error')
            continue

        except requests.exceptions.ReadTimeout:
            print(f'Bad proxy: {address}, timeout reached')
            continue

        if response.json() != sample:
            print(f'Bad proxy: {address}, bad response')
            continue

        print(f"Valid proxy: {address} ({response.elapsed})")
        renew_pool.append(proxy)

    pprint(renew_pool)
    save_to_file(renew_pool)
