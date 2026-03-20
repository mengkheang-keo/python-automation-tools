import requests
from bs4 import BeautifulSoup

url = "https://cccomputerkh.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

html = response.text

soup = BeautifulSoup(html, "html.parser")

products = soup.find_all("div", class_="centerbox1")

data = []
for product in products:
    title_tag = product.find("p", class_="title2")
    price_tag = product.find("span", class_="price2")

    if title_tag and price_tag:
        title = title_tag.text.strip().split("\n")[0]
        price = price_tag.text.strip()

        data.append({
            "title": title,
            "price": price
        })

title_width = max(len(item["title"]) for item in data) + 2
price_width = max(len(item["price"]) for item in data)

total_width = title_width + price_width + 7

print("-" * total_width)
print(f"| {'Product':<{title_width}} | {'Price':>{price_width}} |")
print("-" * total_width)

for item in data:
    print(f"| {item['title']:<{title_width}} | {item['price']:>{price_width}} |")

print("-" * total_width)
print(f"Total products found: {len(data)}")