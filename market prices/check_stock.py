from bs4 import BeautifulSoup as bs
import requests

url = 'https://finance.yahoo.com/most-active?count=100&offset=0'

response = requests.get(url)

soup = bs(response.content, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

# Create a list of stock names and symbols
stocks = []
for row in rows[1:]:
    symbol = row.find('td', {'aria-label': 'Symbol'}).text
    name = row.find('td', {'aria-label': 'Name'}).text
    price = row.find('td', {'aria-label': 'Price (Intraday)'}).text
    stock_info = {'symbol': symbol, 'name': name, 'price': price}
    stocks.append(stock_info)

# Print the list of available stocks
for stock in stocks:
    print(f'{stock["symbol"]} - {stock["name"]}: {stock["price"]}')

print("Bye!")
