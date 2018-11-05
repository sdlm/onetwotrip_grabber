import time
import traceback
from pprint import pprint

import requests


if __name__ == '__main__':

    calendar = {}

    query_params = {
        'ad': '1',
        'cn': '0',
        'in': '0',
        'showDeeplink': 'true',
        'cs': 'E',
        'source': '12trip.us',
        'priceIncludeBaggage': 'false',
        'serpVersion': '300'
    }
    url = 'https://www.onetwotrip.com/_api/searching/startSync4/'
    session = requests.Session()

    for day in range(3, 31):

        time.sleep(30)
        query_params['route'] = f'{day}11LCACEK'
        response = session.post(url=url, verify=False, params=query_params)
        try:
            response_data = response.json()
            if response_data == {'error': 'REQUEST_LIMIT_REACHED'}:
                continue
            try:
                response_data['frs']
            except KeyError:
                pprint(response_data)
                continue
            # pprint(response_data)
            lines = [
                {
                    'price': float(f"{line['prcInf']['amt']:.2f}"),
                    'link': f"https://www.onetwotrip.com{line['deeplink']}",
                }
                for line in response_data['frs']
            ]
            # lines = list(lines)
            # lines.sort()
            best_choice = lines[0]
            for line in lines:
                if line['price'] < best_choice['price']:
                    best_choice = line
            # print('date:', day, 'NOV')
            # print('price:', best_choice['price'])
            # print('link:', best_choice['link'])
            calendar[day] = best_choice['price']
        except Exception:
            traceback.print_exc()
            pass

    pprint(calendar)
