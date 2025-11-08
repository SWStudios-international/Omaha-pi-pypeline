import requests
from bs4 import BeautifulSoup

def get_omaha_pd_calls():
    """Scrapes live Omaha Police calls for service."""
    url = "https://opd.ci.omaha.ne.us/police-calls"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    results = []
    if table:
        for row in table.find_all('tr')[1:]:
            cols = [td.text.strip() for td in row.find_all('td')]
            if cols:
                results.append(cols)
    return results
