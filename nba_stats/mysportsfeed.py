#!/usr/bin/python

import requests
import base64
import json

def main():
    url     = "https://api.mysportsfeeds.com/v1.2/pull/nba/2019-2020-regular/daily_player_stats.csv?fordate=20191130" # modify the fordate to the date you want to pull for this season
    headers = {"Authorization": "Basic " + base64.b64encode('{}:{}'.format({"YOURKEYHERE"},
        {"YOUROTHERKEYHERE"}).encode('utf-8')).decode('ascii')}

    resp = requests.get(url, headers=headers)
    print resp.text

    return

main()
