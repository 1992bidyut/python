import pandas as pd
import requests

# Load the Excel file
df = pd.read_excel('Textile.xlsx')

# Define the API key and base URL
# api_key = 'YOUR_GOOGLE_API_KEY'
base_url = 'https://maps.googleapis.com/maps/api/geocode/json'

# Function to get coordinates
def get_coordinates(address):
    params = {'address': address, 'key': api_key}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

# Apply the function to the address column
# df['Latitude'], df['Longitude'] = zip(*df['Business address'].apply(get_coordinates))
df['Latitude'], df['Longitude'] = zip(*df['Business Name'].apply(get_coordinates))

# Save the results back to a new Excel file
df.to_excel('Textile_with_Coordinates_by_name.xlsx', index=False)
