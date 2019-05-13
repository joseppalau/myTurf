from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# granada code: SPXX0040:1:SP


class WeatherScrapper:

    def __init__(self, code):
        self.code = code

    def simple_get(self, url):
        try:
            with closing(get(url, stream=True)) as resp:
                if self.is_good_response(resp):
                    return resp.content
                else:
                    return None
        except RequestException as e:
            self.log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

    def is_good_response(self, resp):
        content_type = resp.headers['Content-Type'].lower()
        return (resp.status_code == 200
                and content_type is not None
                and content_type.find('html') > -1)

    def log_error(self, e):
        print(e)

    def icons_forecast(self):
        response = self.simple_get(f'https://weather.com/es-US/tiempo/10dias/l/{self.code}')
        html = BeautifulSoup(response, 'html.parser')
        svgs = html.find_all('svg')
        svgs_list = []

        for svg in svgs[0:5]:
            svgs_list.append((svg['class'][0]))

        return svgs_list





