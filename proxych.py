import IP2Proxy as prxy
import os, path

class ValidateProxyIP:

    db = prxy.IP2Proxy()
    db.open(os.path)
    def IsItProxy(_proxy):
        try:
            with prxy.ipaddress(f'{os.getcwd()}\db\GeoLite2-City.mmdb') as reader:
            if prxy.is
        except Exception as ex:
            print(ex)