import json

import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    res = requests.get(IPINFO_URL.format(ip=ip_address))
    ip_map = json.loads(res.content.decode('utf-8'))
    return ip_map.get('country')

