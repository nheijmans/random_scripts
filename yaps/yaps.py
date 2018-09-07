#!/usr/bin/python
# Copyright (c) 2018 nheijmans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import time
import base64
import logging
import requests
from datetime               import datetime

from plugins.find_emails    import *
from plugins.find_onion     import *
from plugins.find_exe       import *
from plugins.find_s3        import *
"""
PasteBin scrape URL return example

[
    {
        "scrape_url": "https://pastebin.com/api_scrape_item.php?i=0CeaNm8Y",
        "full_url": "https://pastebin.com/0CeaNm8Y",
        "date": "1442911802",
        "key": "0CeaNm8Y",
        "size": "890",
        "expire": "1442998159",
        "title": "Once we all know when we goto function",
        "syntax": "java",
        "user": "admin"
    },
    {
        "scrape_url": "https://pastebin.com/api_scrape_item.php?i=8sUIsf34",
        "full_url": "https://pastebin.com/8sUIsf34",
        "date": "1442911665",
        "key": "8sUIsf34",
        "size": "250",
        "expire": "0",
        "title": "master / development delete restriction",
        "syntax": "php",
        "user": ""
    }
]    

"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PasteScraper:
    def __init__(self):
        self.url    = "https://scrape.pastebin.com/api_scraping.php?limit=100"

    def get_pastes(self):
        try:
            recent_pastes = requests.get(self.url,timeout=3.0).json()
        except Exception as e:
            print "[!] {0} error occurred: {1}".format(str(datetime.now()),e)
            recent_pastes = []
        finally:
            return recent_pastes

    def main(self):
        logging.getLogger('urllib3.connectionpool').setLevel(logging.ERROR)
        old_pastes = []

        while True:
            try:
                new_pastes = self.get_pastes()
                pastes = [paste for paste in new_pastes if paste['key'] not in old_pastes]

                print "[*] {0} Parsing {1} pastes...".format(str(datetime.now()), len(pastes))
                for paste in pastes:
                    raw = requests.get(paste['scrape_url'],timeout=5).text
                    find_exe(paste,raw)
                    find_emails(paste,raw)
                    find_s3(paste,raw)
                    find_onion(paste,raw)

                # replace the old 100 keys with the latest 100 keys
                old_pastes = [p['key'] for p in new_pastes]

                # sleep a while before starting all over again
                time.sleep(90)
            except Exception as e:
                print "[!] {0} error occurred: {1}".format(str(datetime.now()),e)
                time.sleep(90)

        return

if __name__ == "__main__":
    ps = PasteScraper()
    ps.main()
