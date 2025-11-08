import requests
from bs4 import BeautifulSoup

def get_douglas_inmates():
    """Scrapes Douglas County corrections roster."""
    url = "https://corrections.dccorr.com/roster.php"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'roster'})
    results = []
    if table:
        for row in table.find_all('tr')[1:]:
            cols = [td.text.strip() for td in row.find_all('td')]
            if cols:
                results.append(cols)
    return results
