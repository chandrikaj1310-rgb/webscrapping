import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(len(response.text))

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")
print("Books found:", len(books))
data=[]
for book, price in zip(books, prices):
    print(book.a["title"], "-", price.text)
    data.append((book.a["title"], price.text))
    import pandas as pd
    df = pd.DataFrame(data, columns=["Book Name", "Price"])
df.to_csv("books.csv", index=False)

print(df)
print("CSV File Created Successfully!")