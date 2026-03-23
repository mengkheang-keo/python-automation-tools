import re
import time
import requests
from bs4 import BeautifulSoup

url = "https://cccomputerkh.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

initial_time = time.time()

response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_="centerbox1")

# def search product
def search_product(query):
    search_result = []
    keywords = query.lower().split()
    
    for item in data:
        title = item["title"].lower()
        if all(word in title for word in keywords):
            search_result.append(item)

    return search_result

data = []
for product in products:
    title_tag = product.find("p", class_="title2")
    price_tag = product.find("p", class_="sp")

    original_price = "N/A"
    discount_price = "N/A"

    if price_tag:
        raw_text = price_tag.get_text()
        prices = re.findall(r"\$\d{1,3}(?:,\d{3})*", raw_text)

        # fallback: check span
        span = price_tag.find("span", class_="price2")
        if span and span.text.strip():
            span_price = span.text.strip()
            if span_price not in prices:
                prices.insert(0, span_price)

        if len(prices) == 1:
            original_price = prices[0]
        elif len(prices) >= 2:
            original_price = prices[0]
            discount_price = prices[1]

    if title_tag and price_tag:
        title = title_tag.text.strip().split("\n")[0]

        # skip completely broken entries
        if original_price == "N/A" and discount_price == "N/A":
            continue

        data.append({
            "title": title,
            "original": original_price
        })

# widths
title_width = max(len(item["title"]) for item in data) + 2
original_width = max(len(item["original"]) for item in data)

total_width = title_width + original_width + 7

# main table
print("-" * total_width)
print(f"| {'Product':<{title_width}} | {'Price':>{original_width}} |")
print("-" * total_width)

for item in sorted(data, key=lambda item: item["title"].lower()):
    print(f"| {item['title']:<{title_width}} | {item['original']:>{original_width}} |")

print("-" * total_width)
print(f"Total products found: {len(data)}")
print(f"Total time: {time.time() - initial_time:.2f}s")
print("-" * total_width)

# search
while True:
    search_option = input("\n🔎 Search (type 'exit' or 'sort' or 'search asus laptop'): ").lower().strip()

    if search_option == "":
        print("Incorrect input!")
        continue

    elif search_option == "search":
        print("Please use search param, example: search asus gaming laptop")
        continue

    search_option_parts = search_option.split()
    command = search_option_parts[0]
    search_query = search_option_parts[1:]
    query = " ".join(search_query)

    if command in ['exit', 'quit']:
        print("Exiting...")
        break
    elif command == "sort":
        print("🔍 Sorted by price")

        print("-" * total_width)
        print(f"| {'Product':<{title_width}} | {'Price':>{original_width}} |")
        print("-" * total_width)

        for item in sorted(data, key=lambda item: int(item["original"].replace("$","").replace(",","")) if item["original"] != "N/A" else float('inf')):
            print(f"| {item['title']:<{title_width}} | {item['original']:>{original_width}} |")

        print("-" * total_width)

    elif command == "search":
        results = search_product(query)

        if results:
            print("🔍Results for:", query)
            print("-" * total_width)
            print(f"| {'Product':<{title_width}} | {'Price':>{original_width}} |")
            print("-" * total_width)

            for item in sorted(results, key=lambda item: item["title"].lower()):
                print(f"| {item['title']:<{title_width}} | {item['original']:>{original_width}} |")

            print("-" * total_width)
            print(f"Found {len(results)} matching products")
        else:
            print("❌ No matching products found.")