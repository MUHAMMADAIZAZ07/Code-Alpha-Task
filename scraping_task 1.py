import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "http://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

print("Books Found:", len(books))

data = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text.strip()

    # ✅ CLEAN PRICE (WORKS FOR ALL CASES)
    price = re.sub(r'[^\d.]', '', price)
    price = float(price)

    data.append([title, price])

df = pd.DataFrame(data, columns=["Title", "Price"])

print(df.head())

df.to_csv("books.csv", index=False, encoding='utf-8')

print("CSV file successfully created!")