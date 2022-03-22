import geoip2.database, json, os, re

def ModelResponseToJSON(response):
    pattern = "(\w.{1,}\()|(,\s\['\w+']\))"
    response = re.sub(pattern, '', str(response))
    return json.loads(response.replace("'",'"'))

with geoip2.database.Reader(f'{os.getcwd()}\db\GeoLite2-City.mmdb') as reader:
    response = ModelResponseToJSON(reader.city('8.8.8.8')) 
    print(response)
    
    #latitude = response['location']['latitude']
    #longitude = response['location']['longitude']
    #print(f'Latitude: {latitude}\nLongitude: {longitude}')
    


