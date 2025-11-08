import requests
from bs4 import BeautifulSoup

def craigslist_search(query, location="omaha"):
    url = f"https://{location}.craigslist.org/search/sss?query={query.replace(' ', '+')}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for post in soup.find_all('li', class_='result-row'):
        title_tag = post.find('a', class_='result-title')
        if title_tag:
            title = title_tag.text
            link = title_tag.get('href')
        else:
            title, link = "", ""
        time_tag = post.find('time')
        date = time_tag['datetime'] if time_tag else ""
        results.append({'title': title, 'link': link, 'date': date})
    return results
