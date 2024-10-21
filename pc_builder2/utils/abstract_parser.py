import requests
from bs4 import BeautifulSoup
from django.db import models

class AbstractRequestParser:

    url: str
    model: type[models.Model]
    
    def parse(self):
        self.retreive_data()
        self.divide_data()
        self.load_to_db()

    def retreive_data(self) -> str:
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
        self.prepare(response)

    def extraction()->list[dict]:
        raise NotImplementedError()

    def prepare(self, response):
        self.data = response.json()
        self.soup_data = BeautifulSoup(response.json()['txt'], 'html.parser')
    
    def load_to_db(self):
        data = self.extraction()
        self.model.objects.bulk_create(self.model(**item) for item in data)


    def divide_data(self):
        raise NotImplementedError()
