import requests
from requests.exceptions import ProxyError

ONETWOTRIP_URL = 'https://www.onetwotrip.com/_api/searching/getQuickResult/'
TWOIP_URL = 'https://2ip.ru/'


'''
curl 'https://www.onetwotrip.com/_api/searching/getQuickResult/?route=2711LCACEK&ad=1&cn=0&in=0&showDeeplink=true&cs=E&source=12trip.us&priceIncludeBaggage=false&serpVersion=300&srcmarker=duckduckgo.com%7C%2Fen-us%2F&noCache=true' 
-H 'Host: www.onetwotrip.com' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0' 
-H 'Accept: */*' 
-H 'Accept-Language: en-US,en;q=0.5' --compressed 
-H 'Referer: https://www.onetwotrip.com/en-us/f/flights/larnaca-chelyabinsk_LCA-CEK/' 
-H 'Cookie: referrer_mrk=duckduckgo.com|/en-us/; TrackJS=5c887565-9c75-4fa7-b86e-3c5bb94a6952; km_ai=%2F964AQttz2B5%2BXUtpamn3IrVxJk%3D; km_lv=x; cookiePolicyBannerLastPage=%2F; vid=de5cdf59-0f79-4f4b-b404-276941423d62; _ga=GA1.2.2027491411.1538902421; _gac_UA-21448683-1=1.1538902421.EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; __ssid=d2a6deedabd74a018cb8c4d1b3cf242; routes=%5B%2220181103LCACEK%22%5D; km_lv=1538902592; src_ref=https://www.onetwotrip.com/en-ie/?scp=14%2Cgoogle_adwords_brand%2Cbrand_int&gclid=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; km_uq=1541236974%20%2Fe%3Fdiff%3Dundefined%26currency%3Dundefined%26directionIndex%3D0%26serpVersion%3D300%26page%3DMAIN%26vid%3Dde5cdf59-0f79-4f4b-b404-276941423d62%26Language%3Dru%26lang%3Dru%26locale%3Dru%26EventHour%3D12%26user_agent%3DMozilla%252F5.0%2520(X11%253B%2520Linux%2520x86_64%253B%2520rv%253A58.0)%2520Gecko%252F20100101%2520Firefox%252F58.0%26KM_user_id%3Da779c990-f7dc-8f84-3aa8-72b505375a32%26c_email%3Dnot_logged%26_n%3Dserp_cal_min_date%26_k%3D8d1f8584cbc0a025b95e59b6a64a8e66f864680f%26_p%3D%252F964AQttz2B5%252BXUtpamn3IrVxJk%253D%26_t%3D1541236974%7C1541237206%20%2Fe%3Fdiff%3Dundefined%26currency%3Dundefined%26directionIndex%3D0%26serpVersion%3D300%26page%3DMAIN%26vid%3Dde5cdf59-0f79-4f4b-b404-276941423d62%26Language%3Dru%26lang%3Dru%26locale%3Dru%26EventHour%3D12%26user_agent%3DMozilla%252F5.0%2520(X11%253B%2520Linux%2520x86_64%253B%2520rv%253A58.0)%2520Gecko%252F20100101%2520Firefox%252F58.0%26KM_user_id%3Da779c990-f7dc-8f84-3aa8-72b505375a32%26c_email%3Dnot_logged%26_n%3Dserp_cal_min_date%26_k%3D8d1f8584cbc0a025b95e59b6a64a8e66f864680f%26_p%3D%252F964AQttz2B5%252BXUtpamn3IrVxJk%253D%26_t%3D1541237206; serpVersionSelected=true; referrer_first=google_adwords_brand; referrer_hist=12trip.us|organic_us|12trip.us|google_adwords_brand; ENVID=production-a|W91o9; kvcd=1541231349236; _sst=1538902420406|1540735571186|c65da634a3a1eab7567d00a9f49e713e; viscnt=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; session_ref=https://www.onetwotrip.com/en-ie/?scp=14%2Cgoogle_adwords_brand%2Cbrand_int&gclid=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; amup=ab2; referrer=12trip.us; accept_language=en-us; abst=T_b,ZP_b,serp_300,sm_n,ffp_t; serpVersion=300; tvc=1; sid=8x35DoMybmougxnMY3ET6YVN; _gid=GA1.2.498666983.1541231350; km_user_packages_id=a779c990-f7dc-8f84-3aa8-72b505375a32' 
-H 'Connection: keep-alive'
'''

proxies = {
  'https': 'socks5://206.189.101.248:1080',
}


if __name__ == '__main__':

    # resp = requests.get(url='https://2ip.ru', verify=False)
    # page = resp.text

    result = {}

    query_params = {
        'ad': '1',
        'cn': '0',
        'cs': 'E',
        'in': '0',
        'showDeeplink': 'true',
        'source': '12trip.us',
        'priceIncludeBaggage': 'false',
        'serpVersion': '300',
        'noCache': 'false'
    }

    headers = {
        'Host': 'www.onetwotrip.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.onetwotrip.com/en-us/f/flights/larnaca-chelyabinsk_LCA-CEK/',
        'Cookie': 'referrer_mrk=duckduckgo.com|/en-us/; TrackJS=5c887565-9c75-4fa7-b86e-3c5bb94a6952; km_ai=%2F964AQttz2B5%2BXUtpamn3IrVxJk%3D; km_lv=x; cookiePolicyBannerLastPage=%2F; vid=de5cdf59-0f79-4f4b-b404-276941423d62; _ga=GA1.2.2027491411.1538902421; _gac_UA-21448683-1=1.1538902421.EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; __ssid=d2a6deedabd74a018cb8c4d1b3cf242; routes=%5B%2220181103LCACEK%22%5D; km_lv=1538902592; src_ref=https://www.onetwotrip.com/en-ie/?scp=14%2Cgoogle_adwords_brand%2Cbrand_int&gclid=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; km_uq=1541236974%20%2Fe%3Fdiff%3Dundefined%26currency%3Dundefined%26directionIndex%3D0%26serpVersion%3D300%26page%3DMAIN%26vid%3Dde5cdf59-0f79-4f4b-b404-276941423d62%26Language%3Dru%26lang%3Dru%26locale%3Dru%26EventHour%3D12%26user_agent%3DMozilla%252F5.0%2520(X11%253B%2520Linux%2520x86_64%253B%2520rv%253A58.0)%2520Gecko%252F20100101%2520Firefox%252F58.0%26KM_user_id%3Da779c990-f7dc-8f84-3aa8-72b505375a32%26c_email%3Dnot_logged%26_n%3Dserp_cal_min_date%26_k%3D8d1f8584cbc0a025b95e59b6a64a8e66f864680f%26_p%3D%252F964AQttz2B5%252BXUtpamn3IrVxJk%253D%26_t%3D1541236974%7C1541237206%20%2Fe%3Fdiff%3Dundefined%26currency%3Dundefined%26directionIndex%3D0%26serpVersion%3D300%26page%3DMAIN%26vid%3Dde5cdf59-0f79-4f4b-b404-276941423d62%26Language%3Dru%26lang%3Dru%26locale%3Dru%26EventHour%3D12%26user_agent%3DMozilla%252F5.0%2520(X11%253B%2520Linux%2520x86_64%253B%2520rv%253A58.0)%2520Gecko%252F20100101%2520Firefox%252F58.0%26KM_user_id%3Da779c990-f7dc-8f84-3aa8-72b505375a32%26c_email%3Dnot_logged%26_n%3Dserp_cal_min_date%26_k%3D8d1f8584cbc0a025b95e59b6a64a8e66f864680f%26_p%3D%252F964AQttz2B5%252BXUtpamn3IrVxJk%253D%26_t%3D1541237206; serpVersionSelected=true; referrer_first=google_adwords_brand; referrer_hist=12trip.us|organic_us|12trip.us|google_adwords_brand; ENVID=production-a|W91o9; kvcd=1541231349236; _sst=1538902420406|1540735571186|c65da634a3a1eab7567d00a9f49e713e; viscnt=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; session_ref=https://www.onetwotrip.com/en-ie/?scp=14%2Cgoogle_adwords_brand%2Cbrand_int&gclid=EAIaIQobChMIrKWNnfrz3QIVCflRCh1-hAC9EAAYASAAEgLfCPD_BwE; amup=ab2; referrer=12trip.us; accept_language=en-us; abst=T_b,ZP_b,serp_300,sm_n,ffp_t; serpVersion=300; tvc=1; sid=8x35DoMybmougxnMY3ET6YVN; _gid=GA1.2.498666983.1541231350; km_user_packages_id=a779c990-f7dc-8f84-3aa8-72b505375a32',
        'Connection': 'keep-alive',
    }

    for day in range(8, 31):
        print(f'check price for: {day} NOV')
        query_params['route'] = f'{day:0>2}11LCACEK'

        resp = None
        tries = 3
        while tries > 0:
            try:
                resp = requests.get(ONETWOTRIP_URL, params=query_params, headers=headers, proxies=proxies)
            except (ProxyError, ConnectionError, requests.exceptions.ConnectionError):
                print('proxy error, next try ...')
                tries -= 1

        if not resp:
            continue

        in_day_results = []

        data = resp.json()

        if not data:
            continue

        for line in data:
            if len(line['directions']) > 1:
                raise Exception()
            direction = line['directions'][0]
            trips = direction['trips']
            trips_count = len(trips)
            if trips_count > 2:
                continue
            in_day_results.append({
                'price': line['priceInfo'],
                'trips_count': trips_count,
                'journey_time': direction['journeyTime'],
            })

        currencys = {r['price']['currency'] for r in in_day_results}
        print(currencys)
