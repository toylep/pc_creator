import requests


class AbstractRequestParser:

    url: str

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