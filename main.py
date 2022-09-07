import requests


URL_TEMPLATE = 'https://wttr.in/{}'
LOCATIONS = ('London', 'Череповец', 'svo')


def main():
    for location in LOCATIONS:
        payload = {
            'lang': 'ru',
            'M': '',
            'u': '',
            'n': '',
            'T': '',
            'q': '',

        }
        url = URL_TEMPLATE.format(location)
        response = requests.get(url, params=payload)
        response.raise_for_status()


if __name__ == '__main__':
    main()
