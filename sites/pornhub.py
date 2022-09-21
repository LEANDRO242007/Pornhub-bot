import requests
from bs4 import BeautifulSoup


def phub(search):
    url = 'https://es.pornhub.com'

    response = requests.get(url)

    res = response.url + 'video/search?search=' + search.replace(" ", "+")

        # print(res)

    response2 = requests.get(res)

    soup2 = BeautifulSoup(response2.text, 'html.parser')
    # Videos
    sp = soup2.find('ul', attrs={'id': 'videoSearchResult'}).find_all('div', attrs={'class': 'thumbnail-info-wrapper clearfix'})
    # Canales
    # sp2 = soup2.find('ul', attrs={'id': 'videoSearchResult'}).find_all('div', attrs={'class': 'usernameWrap'})
   
    return sp
