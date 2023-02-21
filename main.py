import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

# <div class="supernova-navi-search-tab supernova-navi-search-tab_active"
# data-hh-tab-id="searchVacancy">Вакансии</div>


HOST = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"


def get_headers():
    headers = Headers(browser="firefox", os="win")
    return headers.generate()

respone = requests.get(HOST, headers=get_headers())
hh_main = respone.text

soup = BeautifulSoup(hh_main, features='lxml')

vac_list = soup.find('div', class_='supernova-navi-search-tab supernova-navi-search-tab_active')



# Добрый день!
# Простите, из-за большого количества работы не успел сделать домашнее задание.
# Но думаю ошибка уже изначально в выборе, от чего отталкиваться...