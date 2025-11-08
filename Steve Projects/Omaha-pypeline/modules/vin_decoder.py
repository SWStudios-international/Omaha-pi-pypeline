def flatten_value(val):

    if isinstance(val, str):
        # If more than half of the chars are newlines, flatten it
        if val.count('\n') > len(val) // 4:
            # Remove newlines and spaces, then return as one word
            return val.replace('\n', '').replace(' ', '')
        # Otherwise, just replace newlines with spaces for safety
        return val.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    return val

def decode_vin(vin):
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
    response = requests.get(url)
    data = response.json()
    result = {
        item['Variable']: flatten_value(item['Value'])
        for item in data['Results'] if item['Value']
    }
    return result
