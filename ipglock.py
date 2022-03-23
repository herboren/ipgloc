import geoip2.database, json, os, re, simplekml, csv
from ipaddress import ip_address, IPv4Address

rowcount = 0

# Open MaxMind db for reading
with geoip2.database.Reader(f'{os.getcwd()}\db\GeoLite2-City.mmdb') as reader:
    # Open CSV file for IP table
    with open('ru.csv', encoding='utf-8-sig') as csvd:
            rows = csv.reader(csvd, dialect='excel', delimiter=',', quotechar="|")
            # Get all IPs for validation
            for row in rows:                
                response = reader.city(row[0])
                # Return GeoLocation
                print(f"IP Address: {row[0]}\nCity: {response.city.name}\Lat/Lon: {response.location.latitude}, {response.location.longitude}")
