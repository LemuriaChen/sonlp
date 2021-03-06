
import requests
from lxml import etree
import prettytable as pt
import re


class Abbrev:

    def __init__(self, verbose=True, ):
        self.base_url = 'https://www.allacronyms.com/'
        self.headers = {
            'content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }
        self.verbose = verbose

    def get_abbreviation(self, query: str) -> dict:

        status = 'ok'
        url = self.base_url + '_'.join(query.lower().split(' ')) + '/abbreviated'

        try:
            html = requests.get(url=url, headers=self.headers).text
            items = self.parse(html, url)

            if self.verbose:
                table = pt.PrettyTable()
                table.field_names = ["rating", "abbreviation", "item", "tags", ]
                for item in items:
                    table.add_row(item)
                print(f'Abbreviation for \'{query}\': \n{len(items)} possible ways to abbreviate \'{query}\'.')
                print(table)

            return {'status': status, 'result': items, 'best': items[0][1]}

        except Exception as e:
            status = 'invalid'
            if self.verbose:
                print(f'fail to connect to < {url} > . {e}')
            return {'status': status, 'error_msg': e}

    def get_fullname(self, query: str) -> dict:

        status = 'ok'
        if ' ' in query:
            assert 'query shouldn\'t contains any blank space .'
        url = self.base_url + query.upper()

        try:
            html = requests.get(url=url, headers=self.headers).text
            items = self.parse(html, url)

            if self.verbose:
                table = pt.PrettyTable()
                table.field_names = ["rating", "item", "fullname", "tags", ]
                for item in items:
                    table.add_row(item)
                print(f'Fullname for \'{query}\': \n{len(items)} possible ways to be abbreviated as \'{query}\'.')
                print(table)

            return {'status': status, 'result': items, 'best': items[0][1]}

        except Exception as e:
            status = 'invalid'
            if self.verbose:
                print(f'fail to connect to < {url} > . {e}')
            return {'status': status, 'error_msg': e}

    @staticmethod
    def parse(html, url):

        try:
            elements = etree.HTML(html)
            terms_rating = [eval(element.xpath('string()').replace('\n', '').strip()) for element in elements.xpath(
                "//div[@id='main-content']/div[@class='terms']/"
                "div[@class='terms_rating']/div[@class='terms_row term_rating sdRating']")]
            item_container, item_text, items_tags = [], [], []
            for element in elements.xpath(
                    "//div[@id='main-content']/div[@class='terms']"
                    "/div[@class='terms_items']//tr[@class='terms_row']"):
                item_container.append(element.xpath('td')[0].xpath(
                    "string()").replace('\n', '').strip().replace('&period;', '.'))
                item_text.append(
                    re.sub(r'[+\-].*variants', '', element.xpath('td')[1].xpath(
                        "string(div/div[@class='item_text'])"
                    ).replace('\n', '').strip().replace('&comma;', ',')).strip())
                items_tags.append(
                    element.xpath('td')[1].xpath(
                        "string(div/div[@class='items_tags'])"
                    ).replace('\n', '').strip())
        except Exception as e:
            print(f'fail to parse elements in web pages < {url} > . {e}')
            return []
        items = list(zip(terms_rating, item_container, item_text, items_tags))

        return items


if __name__ == '__main__':

    # given a fullname string, return it's abbreviation
    print(Abbrev().get_abbreviation('china'))

    # given a abbreviation string, return it's fullname
    print(Abbrev().get_fullname('china'))
