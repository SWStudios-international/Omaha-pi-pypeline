import requests
from bs4 import BeautifulSoup

def bing_news_search(query):
    url = f"https://www.bing.com/news/search?q={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    for card in soup.find_all('a', class_='title'):
        results.append({'title': card.text.strip(), 'link': card['href']})
    return results
