import pandas as pd
import requests

# Load the Excel file
df = pd.read_excel('Market.xlsx')

# Define the API key and base URL for Google Places API

base_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'

# Function to get coordinates using business name
def get_coordinates(business_name):
    params = {
        'input': business_name,
        'inputtype': 'textquery',
        'fields': 'geometry',
        'key': api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'candidates' in data and data['candidates']:
            location = data['candidates'][0]['geometry']['location']
            return location['lat'], location['lng']
    return None, None

# Apply the function to the business name column
df['Latitude'], df['Longitude'] = zip(*df['Business Name'].apply(get_coordinates))

# Save the results back to a new Excel file
df.to_excel('Market_with_Coordinates_By_Name.xlsx', index=False)
