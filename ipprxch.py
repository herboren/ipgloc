import IP2Proxy as prxy
import os, path, csv
import keyterms as key

class ValidateProxyIP:    
    # Referer: https://bgp.he.net/AS 55330

    def IsItProxy(): # needs parameter
        # Load keyterms 
        organization = key.KeyTerms().organization 
        
        # Template Paththreat_
        template = f'{os.getcwd()}\\template\Threat_Template.csv'

        db = prxy.IP2Proxy()
        db.open(os.path.join("data", f'{os.getcwd()}\dbs\IP2PROXY-LITE-PX11.BIN')) # Open Binary File

        with open('pubprxy.csv', 'a', encoding='utf-8', newline='') as ips:
            rows = csv.reader(ips, dialect='excel', delimiter=',', quotechar="|")
            with open(template, 'a', encoding='utf-8', newline='') as tt:
                tt_write = csv.writer(tt, dialect='excel')
                for row in rows:                          
                    record = db.get_all(row[1])
                    tdata = [row[0], row[1], record['is_proxy'],record['proxy_type'],record['threat'],record[''],record[''],record[''],record['isp'],record['domamin'],record['as_name'], record['asn'],record['provider'],record[''],record[''],record[''],record['']]              
                    tt_write.writerow(tdata)
        

    IsItProxy()