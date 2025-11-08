import requests
from bs4 import BeautifulSoup

def nicb_vincheck(vin):
    """Checks VIN against NICB's stolen/salvage registry."""
    url = 'https://www.nicb.org/vincheck'
    session = requests.Session()
    page = session.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Find hidden token for form submission (can change)
    token_tag = soup.find('input', {'name': '_token'})
    token = token_tag['value'] if token_tag else ''
    data = {'vin': vin, '_token': token}
    resp = session.post(url, data=data)
    result_soup = BeautifulSoup(resp.text, 'html.parser')
    # Find result text
    res = result_soup.find('div', class_="alert")
    return res.text.strip() if res else "No result / format changed."
