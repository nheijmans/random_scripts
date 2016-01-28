#!/usr/bin/env python
"""
VirusTotal tool for easy use of the API. This script is intended to work as
a CLI tool and to provide a Class object for tools to import. 

Don't forget to add your API key and the daily quotum of 
the public API key when automating searches:
--------------------------------------------
| Request rate  | 4      | requests/minute |
--------------------------------------------
| Daily quota   | 5760   | requests/day    |
--------------------------------------------
| Monthly quota | 178560 | requests/month  |
--------------------------------------------
"""
import requests
import argparse
import json
import os
from hashlib import sha1 as sha1sum
from pprint import pprint

class VirusTotal:
    def __init__(self):
        """ Constructor of the class VirusTotal """
        self.apikey   = ' --- YOUR API KEY HERE --- '
        self.base_url = 'https://www.virustotal.com/vtapi/v2/'

    def sha1hash(self, sample):
        """ Generate a SHA-1 hash of a sample """
        with open(sample, 'rb') as f:
            sha1_hash = sha1sum(f.read()).hexdigest()
        return str(sha1_hash)

    def search(self, sample):
        """ Search for a hash, file or URL """
        # Determine the type of sample and search it accordingly
        if os.path.isfile(sample):
           sample = self.sha1hash(sample)
           ext = 'file/report'
        elif '.' in sample:
           ext = 'url/report'
        else:
           ext = 'file/report'

        payload  = {'resource':sample, 'apikey':self.apikey}
        response = requests.get(self.base_url+ext, params=payload)
        jdata    = json.loads(response.text)

        if jdata['response_code'] == 1:
            return jdata
        else:
            return {'result':None}

    def submit(self, sample):
        """ Submit a file or URL """
        # Determine the type of sample and submit it accordingly
        if os.path.isfile(sample):
            files    = {'file': open(sample, 'rb')}
            response = requests.post(self.base_url+'file/scan', files=files,
                                      params={'apikey':self.apikey})
        elif '.' in sample:
            payload  = {'url':sample, 'apikey':self.apikey}
            response = requests.post(self.base_url+'url/scan', params=payload)
        else:
            return {'error':'unknown type'}
        
        # Return results
        if response.status_code == 200:
            jdata = json.loads(response.text)
            return jdata
        else:
            return {'response':response.status_code}

if __name__ == '__main__':
    vt = VirusTotal()
    parser  = argparse.ArgumentParser(description='VirusTotal API tool',
                                      version='0.1')
    sub     = parser.add_subparsers(help='commands', dest='cmd')
    
    # Search command
    search_parser = sub.add_parser('search', 
                                    help='Search for md5, sha1, sha256 or a URL')

    search_parser.add_argument('sample', action='store', 
                                help='Object to submit (file or URL)')

    # Submit command
    submit_parser = sub.add_parser('submit', 
                                    help='Submit a file or URL to VirusTotal')

    submit_parser.add_argument('sample', action='store', 
                                help='Object to search (file, hash or URL)')
    
    # Process the user input
    args = parser.parse_args()
    if args.cmd == 'search':
        result = vt.search(args.sample)
    elif args.cmd == 'submit':
        result = vt.submit(args.sample)
    else:
        result = {'Error':'You need to tell me what to do! (search or analyze)'}

    # Print the results user-readable
    pprint(result)
