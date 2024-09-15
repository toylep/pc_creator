import requests
from bs4 import BeautifulSoup
import json
import re
class TechCityParser:
    """
    Парсер tech city для получения
    базовых данных о комплектующих и индкексах производительности
    """
    url: str

    def __init__(self,url:str = "https://technical.city/ru/video/rating?pg=1&sort_field=type&sort_order=up&ajax=1"):
        self.url = url

    def parse(self) -> str:
        """Send a GET request to the website and return the HTML response."""
        # url = "https://technical.city/ru/video/rating"

        # Set the User-Agent header to avoid being blocked as a bot
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

        # Set the Accept header to HTML
        accept = "text/html"

        # Create a dictionary of headers to send with the request
        headers = {"Accept": accept, "User-Agent": user_agent}

        # Send the request and get the response
        response = requests.get(self.url, headers=headers)
        # print(response.text)
        
        # Return the HTML content of the response
        return response.json()['txt']
    
    def extraction(self):

        response = self.parse()

        soup = BeautifulSoup(response, 'html.parser')
        # считываем заголовок страницы
        cards = soup.find_all('tr')  # Поиск карточек видеокарт
        card_list = []

        for card in cards:
            try:
                cells = card.find_all('td')
                name = cells[1].find('a')
                performance = cells[3]
                power = cells[6]

                if (
                    name is None 
                    or performance is None 
                    or power is None
                    ):
                    continue
                
                name = name.text.strip() 
                performance = performance.text.strip() 
                power = power.text.strip()[:-2] 
                print("power", power)
                print("name", name)
                print("performance", performance)

                card_json={
                    "name":name,
                    "performance":performance,
                    "power": int(power)
                }
                print(card_json)
                card_list.append(card_json)
            except IndexError: 
                continue
            

       
        # print(type(cards))

        return card_list