#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from datetime import datetime

def main():
    #url   = "https://www.basketball-reference.com/leagues/NBA_2018_per_game.html#per_game_stats::none"
    url    = "https://www.basketball-reference.com/leagues/NBA_2019_per_game.html#per_game_stats::none"
    raw   = requests.get(url,timeout=3)
    soup  = BeautifulSoup(raw.text,"lxml")
    table = soup.find('table')
    time  = datetime.utcnow()
    ts    = "{0}-{1}-{2}".format(time.year,time.month,time.day)

    table_body = table.find('tbody')
    players = []
    for row in table_body.findAll('tr'):
        player_data = OrderedDict()
        player_url = row.find('a')
        if player_url:
            player_name = player_url.text
            cells = row.findAll('td')
            player_data['name']         = cells[0].text
            player_data['pos']          = cells[1].text
            player_data['age']          = cells[2].text
            player_data['team']         = str(cells[3].text)
            player_data['g']            = cells[4].text
            player_data['gs']           = cells[5].text
            player_data['mp_per_g']     = cells[6].text
            player_data['fg_per_g']     = cells[7].text
            player_data['fg_pct']       = cells[8].text
            player_data['fg3_per_g']    = cells[9].text
            player_data['fg3a_per_g']   = cells[10].text
            player_data['fg3_pct']      = cells[11].text
            player_data['fg2_per_g']    = cells[12].text
            player_data['fg2a_per_g']   = cells[13].text
            player_data['fg2_pct']      = cells[14].text
            player_data['efg_pct']      = cells[15].text
            player_data['ft_per_g']     = cells[16].text
            player_data['fta_per_g']    = cells[17].text
            player_data['ft_pct']       = cells[18].text
            player_data['orb_per_g']    = cells[19].text
            player_data['drb_per_g']    = cells[20].text
            player_data['trb_per_g']    = cells[21].text
            player_data['ast_per_g']    = cells[22].text
            player_data['stl_per_g']    = cells[23].text
            player_data['blk_per_g']    = cells[24].text
            player_data['tov_per_g']    = cells[25].text
            player_data['pf_per_g']     = cells[26].text
            player_data['pts_per_g']    = cells[27].text
            players.append(player_data)
        else:
            pass

    # write csv
    headers = ['player', 'pos', 'age', 'tm', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', '3p', '3pa', '3p_pct', '2p', '2pa', '2p_pct', 'efg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'ps_per_g']
    with open("logs/nba_daily_stats_{0}.csv".format(ts),"w") as ofile:
        ofile.write(','.join(headers)+"\n")

        for player in players:
            try:
                text = ""
                for k,v in player.items():
                    text = text+","+'"'+v+'"'
                ofile.write(text[1:]+"\n")
            except:
                pass


    print "done!"

                
    return

main()
