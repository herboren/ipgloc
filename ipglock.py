import geoip2.database, json, os, re, csv
from ipaddress import ip_address, IPv4Address

uscenter = '207.250.97.159'
# 38.2507,-85.7472
# Louisville, KY

# Open MaxMind db for reading
with geoip2.database.Reader(f'{os.getcwd()}\db\GeoLite2-City.mmdb') as reader:
    # Open CSV file for IP table
    with open('ru.csv', encoding='utf-8-sig') as csvd:
            rows = csv.reader(csvd, dialect='excel', delimiter=',', quotechar="|")
            # Get all IPs for validation
            for row in rows:    
                try:            
                    response = reader.city(row[0])
                    # Return GeoLocation
                    print(f"IP Address: {row[0]}\n\nCity: {response.city.name}\nLat/Lon: {response.location.latitude}, {response.location.longitude}")
                except Exception as ex:
                    print()
