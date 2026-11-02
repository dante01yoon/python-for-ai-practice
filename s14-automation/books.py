import httpx
from bs4 import BeautifulSoup

html = httpx.get("https://books.toscrape.com/", timeout=10).text
soup = BeautifulSoup(html, "html.parser")

for book in soup.select("article.product_pod")[:5]:
    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    print(f"{price:>8}  {title}")
