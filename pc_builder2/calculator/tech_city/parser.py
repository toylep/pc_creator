import requests
from bs4 import BeautifulSoup
from utils.abstract_parser import AbstractRequestParser
class TechCityParser(AbstractRequestParser):
    """
    Парсер tech city для получения
    базовых данных о комплектующих и индкексах производительности
    """
    url: str = "https://technical.city/ru/video/rating?pg=1&sort_field=type&sort_order=up&ajax=1"


    
    def validate(self):
        








        return 
    def extraction(self):

        response = self.parse()

        soup = BeautifulSoup(response, 'html.parser')
        # считываем заголовок страницы
        
        cards = soup.find_all('tr') # Поиск карточек видеокарт
        
        card_list = []

        for card in cards:
                
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


                card_json={
                    "name":name,
                    "performance":performance,
                    "power": int(power)
                }
                print(card_json)
                card_list.append(card_json)
            
            

       
        # print(type(cards))

        return card_list