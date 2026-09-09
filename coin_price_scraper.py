import requests
import csv
import json
from datetime import datetime

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'price_change_percentage': '24h',
}
def fetch_data():
    response = requests.get(url, params=params)
    data = response.json()
    return data
def write_to_csv(data):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'coin_prices_{timestamp}.csv'

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Symbol', 'Current Price', 'Market Cap', '24H Change (%)'])

        for entry in data:
            writer.writerow([
                entry['name'],
                entry['symbol'],
                entry['current_price'],
                entry['market_cap'],
                entry['price_change_percentage_24h'],
            ])

    print(f'Data written to {filename}')

if __name__ == '__main__':
    data = fetch_data()
    write_to_csv(data)
