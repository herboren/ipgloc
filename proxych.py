import IP2Proxy as prxy
import os, path, csv
import keyterms as key

class ValidateProxyIP:    
    # Referer: https://bgp.he.net/AS 55330

    def IsItProxy(): # needs parameter

        # Get header and keyterms
        csv_header = key.KeyTerms().proxy_csv_header   
        organization = key.KeyTerms().organization 

        db = prxy.IP2Proxy() # Object
        db.open(os.path.join("data", f'{os.getcwd()}\dbs\IP2PROXY-LITE-PX11.BIN'))

        tdata = {}

        with open('pubprxy.csv', encoding='utf-8-sig') as csv_data:
            rows = csv.reader(csv_data, dialect='excel', delimiter=',', quotechar="|")
            for row in rows:
                try:
                    tdata = db.get_all(row[0])
                    for cell in tdata:
                        #for k,v in organization.items():
                            #if k in str(tdata[cell]):
                        print(f'{cell}: {tdata[cell]}')
                        # needs to pass data as an array back to ipcloc, to store in csv.
                except Exception as ex:
                    print(ex)

    IsItProxy()