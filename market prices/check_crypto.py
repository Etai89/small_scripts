from bs4 import BeautifulSoup
import requests

# Crypto Currencies
url = 'https://finance.yahoo.com/crypto/?offset=0&count=100'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all price elements on the page
for element in soup.find_all('td', {'aria-label': 'Price (Intraday)'}):
    symbol = element.find('fin-streamer').get('data-symbol') if element.find('fin-streamer') is not None else 'Unknown'
    value = element.find('fin-streamer').text if element.find('fin-streamer') is not None else 'Unknown'
    print(f"Symbol: {symbol}\nPrice: {value}")
    print()
