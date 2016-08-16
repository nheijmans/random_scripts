#!/usr/bin/python
import requests as req

def main(ua):
    payload = { 'uas':ua, 'getJSON':'all' }
    url = 'http://www.useragentstring.com/'
    response = req.get(url, params=payload)
    r = response.json()
    print response.url
    for k,v in r.items():
        print k,':',v


main("Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201")
