import geoip2.database, json, os, re, csv
from ipaddress import ip_address, IPv4Address

uscenter = '207.250.97.159'
csv_header = ['Date and Time','source', 'city', 'country', 'src_latitude', 'src_longitude','tar_latitude','tar_longitude']
# 38.2507,-85.7472
# Louisville, KY

# Open MaxMind db for reading
with geoip2.database.Reader(f'{os.getcwd()}\db\GeoLite2-City.mmdb') as reader:
    # Open CSV file for IP table
    with open('wireshark.csv', encoding='utf-8-sig') as csvd:
        rows = csv.reader(csvd, dialect='excel', delimiter=',', quotechar="|")
        with open('iploc-trkng.csv', 'w', encoding='utf-8', newline='') as iptrk:
            csv_write = csv.writer(iptrk, dialect='excel')
            csv_write.writerow(csv_header)
            # Get all IPs for validation
            for row in rows:   
                try:            
                    response = reader.city(row[2])
                    data = [row[0],row[2],response.city.name,response.country.name,response.location.latitude,response.location.longitude,'38.2507','-85.7472']
                    #print(data)
                    csv_write.writerow(data)
                except Exception as ex:
                    print(ex)
