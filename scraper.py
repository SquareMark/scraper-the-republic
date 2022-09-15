import requests
import lxml.html as html

HOME_URL = 'https://www.larepublica.co'

XPATH_LINK_TO_ARTICLE = '//text-fill/a/@href'
XPATH_TITLE = '//*[@id="vue-container"]/div[3]/div[1]/div[2]/div[1]/h2/span/text()'
XPATH_SUMMARY = '//div[@class = "lead"]/p/text()'
XPATH_BODY = '//div[@class = "html-content"]/p/text()'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()
