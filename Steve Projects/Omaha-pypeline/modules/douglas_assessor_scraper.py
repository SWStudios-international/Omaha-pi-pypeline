import requests
from bs4 import BeautifulSoup

def assessor_search(query):
    """
    Scrapes Douglas County Assessor (propertymax) for an owner name or address.
    Returns list of matching parcels with summary info.
    """
    search_url = "https://douglascounty-ne.propertymax.com/parcelsearch"
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {
        "searchBy": "all",        # Options: all, owner, address, parcel
        "searchTerm": query
    }
    # Submit search form
    resp = session.post(search_url, headers=headers, data=payload)
    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table", class_="parcel-table")
    results = []
    if table:
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if cols:
                summary = {
                    "parcel_id": cols[0].get_text(strip=True),
                    "address": cols[1].get_text(strip=True),
                    "owner": cols[2].get_text(strip=True),
                    "property_type": cols[3].get_text(strip=True),
                    "link": "https://douglascounty-ne.propertymax.com" + cols[0].find('a')['href'] if cols[0].find('a') else ""
                }
                results.append(summary)
    return results

# Example usage (uncomment for testing)
# if __name__ == "__main__":
#     data = assessor_search("your search term here")
#     for r in data:
#         print(r)
