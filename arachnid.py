import urllib.request
from bs4 import BeautifulSoup
from tacoshell import taco_wrap


url = 'https://www.vg.no'
variables = [{'name': 'url', 'type': 'StringVar', 'value': url}]
settings = [{'name': 'element_source',
             'kwargs': {'handle': 'test', 'var': 'url'}}]


@taco_wrap(variables, settings)
def request():
    use_proxy = False  # Must be on while inside corporate network
    if use_proxy:
        # http://proxyconf-uba.siemens.net/proxy-coia.pac
        proxy = urllib.request.ProxyHandler({'http': 'http://194.138.0.7:9400',
                                             'https': 'http://194.138.0.8:9400'})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener)

    response = urllib.request.urlopen(url)
    bytes_ = response.read()
    html = bytes_.decode("utf8")

    soup = BeautifulSoup(html)
    links = soup.find_all('a')
    result = []
    for tag in links:
        link = tag.get('href', None)
        if link is not None:
            if not str(link).endswith('/'):
                if link not in result:
                    result.append(link)
    for l in result:
        print(l)
    return result


if __name__ == '__main__':
    request()
