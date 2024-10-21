from django.db.models.base import Model as Model
import requests
from utils.abstract_parser import AbstractRequestParser
from calculator.models import BaseGPU
class TechCityGPUParser(AbstractRequestParser):
    """
    Парсер tech city для получения
    базовых данных о комплектующих и индкексах производительности
    """
    url: str = "https://technical.city/ru/video/rating?pg=1&sort_field=type&sort_order=up&ajax=1"
    model = BaseGPU
    
    def divide_data(self):
        self.soup_data = self.soup_data.find_all('tr')
        
    def extraction(self):
        card_list = []
        for card in self.soup_data:
            if card is not None and card.has_attr('data-id'):
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
                try:
                    power = int(power)    
                except ValueError:
                    power = None
                card ={
                    "short_name": name,
                    "perfomance_index":performance,
                    "tdp": power
                }
                card_list.append(card)   
        
        return card_list    
