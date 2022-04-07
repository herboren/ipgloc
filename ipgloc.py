import geoip2.database, json, os, re, csv, path
from ipaddress import ip_address, IPv4Address
import IP2Proxy as prxy
import kterms as key

# Initialize Column Header
csv_header = key.KeyTerms().report_columns

# Set path to csv output
threat_data_csv = f'{os.getcwd()}\\csv\\threat_data.csv' # Output

# Check for output csv, create if not exists
if not os.path.exists(threat_data_csv):
    f = open(threat_data, 'w')
    f.close()

    # Add columns to csv output
    with open(threat_data_csv, 'w', encoding='utf-8', newline='') as threat_data:   
        td_wrtr = csv.writer(threat_data, dialect='excel')
        td_wrtr.writerow(csv_header)

# Initialize log data to read
wireshark_data  = f'{os.getcwd()}\\csv\\wireshark_data.csv'
public_proxies  = f'{os.getcwd()}\\csv\\public_proxies.csv'
russian_ips     = f'{os.getcwd()}\\csv\\public_proxies.csv'

# Lets get IPs in log
def GetIpData(csv_data):
    # Open CSV file for IP table
        with open(f'{os.getcwd()}\csv\wireshark_data.csv', encoding='utf-8-sig') as wireshark_data:
            rows = csv.reader(wireshark_data, dialect='excel', delimiter=',', quotechar="|")
            
            # Get all IPs for validation
            for row in rows:         
                    # Get response data, if IP exists
                    csv_data.writerow(GetIpLocationData(row[2]))
                    

# Lets get physical location data
def GetIpLocationData(ip):
    # Open DB for reading Geolocation
    with geoip2.database.Reader(f'{os.getcwd()}\dbs\GeoLite2-City.mmdb') as geolocator:
        # Open CSV file for IP table
        try:       
            # Get response data, if IP exists
            response = geolocator.city(ip)
            # Build template
            return [row[0],row[2],response.city.name,response.country.name,response.location.latitude,response.location.longitude,'38.2507','-85.7472']               
        except Exception as ex:
            print(ex)

GetIpData(threat_data_csv)