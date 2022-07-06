import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"}
for n in range(1, 2):
    sleep(3)
    url = f"https://barnaul.parosigara.ru/catalog/veypy/?PAGEN_1={n}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find_all('div', class_='item_block col-4 col-md-3 col-sm-6 col-xs-6')

    for i in data:
        card_url = "https://barnaul.parosigara.ru" + i.find('a').get('href')
        list_card_url.append(card_url) #Получаем список карточек товаров

for card_url in list_card_url: #Парсинг каждой карточки товара
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find('div', class_="wraps hover_blink")

    title = data.find("h1").text
    price = data.find('div', class_='price').text
    store_view = data.find('span', class_='store_view').text
    discription = data.find('div', class_='col-md-12').text
    img = 'https://barnaul.parosigara.ru' + data.find('div', class_='slides').find('li').find('link').get('href')
    print(title + '\n' + price + '\n' + store_view + '\n' + discription + '\n' + img + '\n\n')
