import requests

class DataFetcher:
    def __init__(self, api_key, city):
        self.api_key = api_key
        self.city = city

    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        data = response.json() # 받아온 데이터를 JSON으로 변경해서 data 저장.
        
        return data