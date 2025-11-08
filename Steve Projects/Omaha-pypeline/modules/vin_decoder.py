import requests

def decode_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
    response = requests.get(url)
    data = response.json()
    result = {item['Variable']: item['Value'] for item in data['Results'] if item['Value']}
    return result
