from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
quotes = soup.findAll("span", attrs={'class': "text"})
authors = soup.findAll("small", attrs={'class': "author"})

for quote, author in zip(quotes, authors):
    print(zip(quotes, authors))
    print(quote.text + "-"+author.text)
