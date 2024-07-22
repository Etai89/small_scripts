from bs4 import BeautifulSoup
import requests

# World Indices
url = 'https://finance.yahoo.com/world-indices'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all fin-streamer elements on the page
for element in soup.find_all('tr', {'class': 'simpTblRow'}):
    name = element.find('td', {'aria-label': 'Name'}).text if element.find('td', {'aria-label': 'Name'}) is not None else 'Unknown'
    symbol = element.find('td', {'aria-label': 'Symbol'}).text if element.find('td', {'aria-label': 'Symbol'}) is not None else 'Unknown'
    value = element.find('td', {'aria-label': 'Last Price'}).text if element.find('td', {'aria-label': 'Last Price'}) is not None else 'Unknown'
    change = element.find('td', {'aria-label': 'Change'}).text if element.find('td', {'aria-label': 'Change'}) is not None else 'Unknown'
    print(f"Index: {name}\nSymbol: {symbol}\nPrice: {value}\nChange: {change}")
    print()
