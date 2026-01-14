import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "http://quotes.toscrape.com"

# Send HTTP request
response = requests.get(URL)
response.raise_for_status()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

# Extract quotes
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]

    quotes_data.append({
        "quote": text,
        "author": author,
        "tags": ", ".join(tags)
    })

# Save as CSV
df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)

# Save as JSON
df.to_json("quotes.json", orient="records", indent=4)

print("Scraping completed! Data saved to quotes.csv and quotes.json")
