import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}

def download(url):
    resp = requests.get(url, stream=True)
    r = open('C:\\Users\\1F1T1\Desktop\\image\\' + url.split('/')[-1], 'wb')
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():
    url = 'https://altapress.ru/'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    for i in range(2, 6):
        data = soup.find_all('div', class_=f'post_item cell_type_1 post_item_{i} col-xl-3 col-3')
        for ii in data:
            card_url = "https://altapress.ru" + ii.find('a').get('href')
            print(card_url)
print(get_url())
# def array():
#     for card_url in get_url():
#
#         response = requests.get(card_url, headers=headers)
#         sleep(1)
#         soup = BeautifulSoup(response.text, 'lxml')
#
#
#         data = soup.find('div', class_='b-post story')
#         title = data.find('h1').text
#         text = data.find('div', class_='bb_phrase').text
#         #url_image = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
#         #download(url_image)
#         return title, tedxt

#print(array())