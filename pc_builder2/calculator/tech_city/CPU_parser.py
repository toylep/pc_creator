from django.db.models.base import Model as Model
import requests
from utils.abstract_parser import AbstractRequestParser
from calculator.models import BaseCPU
class TechCityCPUParser(AbstractRequestParser):
    """
    Парсер tech city для получения
    базовых данных о комплектующих и индкексах производительности
    """
    url: str = "https://technical.city/ru/cpu/rating?pg=1&sort_field=type&sort_order=up&ajax=1"
    model = BaseCPU
    
    def divide_data(self):
        self.soup_data = self.soup_data.find_all('tr')
        
    def extraction(self):
        CPU_list = []
        for CPU in self.soup_data:
            if CPU is not None and CPU.has_attr('data-id'):
                cells = CPU.find_all('td')

                name = cells[1].find('a')
                socket = cells[3]
                performance = cells[4]
                power = cells[7]

                if (
                    name is None or
                    socket is None
                    or performance is None 
                    or power is None
                    ):
                    continue

                name = name.text.strip() 
                socket = socket.text.strip()
                performance = performance.text.strip() 
                power = power.text.strip()[:-2] 
                try:
                    power = int(power)    
                except ValueError:
                    power = None
                CPU ={
                    "name": name,
                    "perfomance_index":performance,
                    "socket": socket,
                    "tdp": power
                }
                CPU_list.append(CPU)   
        
        return CPU_list    
