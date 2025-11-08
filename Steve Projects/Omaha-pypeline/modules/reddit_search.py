import requests
from bs4 import BeautifulSoup

def reddit_keyword_search(query):
    """Searches Reddit posts via Bing (not direct API)."""
    url = f"https://www.bing.com/search?q=site:reddit.com+{query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    for link in soup.find_all('a'):
        href = link.get('href', '')
        if 'reddit.com/r/' in href:
            results.append({'title': link.text.strip(), 'link': href})
    return results
