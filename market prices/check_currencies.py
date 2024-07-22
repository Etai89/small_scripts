from bs4 import BeautifulSoup
import requests

# Currencies
url = 'https://finance.yahoo.com/currencies'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all last price elements on the page
for element in soup.find_all('td', {'aria-label': 'Last Price'}):
    symbol = element.find('fin-streamer').get('data-symbol') if element.find('fin-streamer') is not None else 'Unknown'
    value = element.find('fin-streamer').text if element.find('fin-streamer') is not None else 'Unknown'
    print(f"Symbol: {symbol}\nLast Price: {value}")
    print()
