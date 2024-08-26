import googlemaps
import csv

# Google Places API key
api_key = 'YOUR_API_KEY'

# Initialize the client
gmaps = googlemaps.Client(key=api_key)

# Define your search parameters
location = 'YOUR_LOCATION'
radius = 1000  # in meters, adjust as needed
query = 'YOUR_KEYWORD'

# Perform a nearby search
places = gmaps.places_nearby(location=location, radius=radius, keyword=query)

# Create a CSV file to write the results
with open('companies_without_website.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Company Name', 'Phone Number', 'Address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through the results
    for place in places['results']:
        name = place['name']
        phone_number = place.get('formatted_phone_number', 'N/A')
        address = place.get('vicinity', 'N/A')
        website = place.get('website', 'N/A')

        # Write only businesses without a website to the CSV file
        if website == 'N/A':
            writer.writerow({'Company Name': name, 'Phone Number': phone_number, 'Address': address})

print("CSV file has been generated successfully.")
