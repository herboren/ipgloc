import IP2Proxy as prxy
import os, path, csv

class ValidateProxyIP:

    columns = {
        'IP','Is Proxy','Proxy Type','Country Name','Region Name','City Name','ISP',
        'Domain','Usage Type', 'ASN','AS Name','Last Seen','Threat','Provider'
    }
    
    def IsItProxy():
        db = prxy.IP2Proxy()
        db.open(os.path.join("data", f'{os.getcwd()}\dbs\IP2PROXY-LITE-PX11.BIN'))

        tdata = []
        try:
            tdata = db.get_all('169.57.1.85')
            for cell in tdata:
                print(f'{cell}: {tdata[cell]}\n')

            print(tdata)
        except Exception as ex:
            print(ex)

    IsItProxy()