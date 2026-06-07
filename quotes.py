# Import required libraries
import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}/"
headers = {"User-Agent": "Mozilla/5.0"}

all_quotes = []

# Loop through first 10 pages of quotes
for page_num in range(1, 11):
    url = base_url.format(page_num)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')

    contents = soup.find_all('div', class_='quote')

    for data in contents:
        quote = data.find('span', class_='text').text.strip()
        author = data.find('small', class_='author').text.strip()
        tags = [tag.text for tag in data.find_all('a', class_='tag')]

        # Replace curly quotes to avoid CSV formatting issues
        quote = quote.replace('“', '"').replace('”', '"')

        all_quotes.append([quote, author, ', '.join(tags)])

# Write results to CSV with proper encoding for Excel compatibility
with open('quotes.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(['Quote', 'Author', 'Tags'])
    writer.writerows(all_quotes)