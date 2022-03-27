class KeyTerms:

    organization = {
        "COM":"Commercial",
        "ORG":"Organization",
        "GOV":"Government",
        "MIL":"Military",
        "EDU":"University/College/School",
        "LIB":"Library",
        "CDN":"Content Delivery Network",
        "ISP":"Fixed Line ISP",
        "MOB":"Mobile ISP",
        "DCH":"Data Center/Web Hosting/Transit",
        "SES":"Search Engine Spider",
        "RSV":"Reserved"
        }

    proxy_csv_header = [
        'IP','Is Proxy','Proxy Type','Country Name','Region Name','City Name','ISP',
        'Domain','Usage Type', 'ASN','AS Name','Last Seen','Threat','Provider'
        ]

    gloc_csv_header = [
        'Date and Time','source', 'city', 'country', 'src_latitude', 'src_longitude',
        'tar_latitude','tar_longitude'
        ]
    report_columns = [
        'Date_Time','IPv4','Is_Proxy','Proxy','Type','Top_Level','Country',
        'Region','City','ISP','Domain','Organization','ASN_Name','ASN_#','Threat_Type','Provider',
        'IPv4_Latitidue','IPv4_Longitude','Target_Latitude','Target_Longitude'
        ]