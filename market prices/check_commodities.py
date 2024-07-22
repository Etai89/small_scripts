from bs4 import BeautifulSoup
import requests

url = 'https://finance.yahoo.com/commodities'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all table rows
rows = soup.find_all('tr')

# Loop through each row and extract the data
for row in rows[1:]:
    data = row.find_all('td')
    name = data[0].text
    price = data[1].text
    change = data[2].text
    percent_change = data[3].text
    print(f"Commodity: {name}\nPrice: {price}\nChange: {change}\nPercent change: {percent_change}")
    print()
