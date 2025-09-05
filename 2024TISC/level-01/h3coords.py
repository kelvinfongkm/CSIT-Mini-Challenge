import h3

# List of H3 hex addresses
h3_addresses = [
    '8c1e806a3ca19ff',
    '8c1e806a3c125ff',
    '8c1e806a3ca1bff'
]

# Function to convert H3 addresses to latitude and longitude
def h3_to_geo(h3_addresses):
    geo_coords = []
    for address in h3_addresses:
        lat_lng = h3.h3_to_geo(address)  # Converts H3 hex to (latitude, longitude)
        geo_coords.append(lat_lng)
    return geo_coords

# Get the geographic coordinates
coordinates = h3_to_geo(h3_addresses)

# Print the coordinates
for i, coord in enumerate(coordinates, 1):
    print(f"H3 Address {i}: {h3_addresses[i-1]}")
    print(f"Coordinates: Latitude: {coord[0]}, Longitude: {coord[1]}")
    # print(coord[0], coord[1])
