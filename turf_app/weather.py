from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


raw_html = get('https://weather.com/es-US/tiempo/10dias/l/SPXX0040:1:SP')

html = BeautifulSoup(raw_html.content, 'html.parser')

section = html.find(id="main-DailyForecast-1bbda948-59cc-4040-9a36-d9c1ed37a806")

trs = section.find_all('tr')[1:10]

for tr in trs:
    for td in tr.find_all('td'):
        print(td.getText(), end=' | ')
    print()







