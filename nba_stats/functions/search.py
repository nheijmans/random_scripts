"""
Search script for Basketbal Reference
"""

from csv import reader
from operator import itemgetter
def statistics(statistic):
    # read csv
    headers = ['player', 'pos', 'age', 'tm', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', '3p', '3pa', '3p_pct', '2p', '2pa', '2p_pct', 'efg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'ps_per_g']
    with open("logs/nba_daily_stats.csv","r") as ifile:
        data = list(reader(ifile, delimiter=","))
        i = headers.index(statistic)

        # Convert all values to integers
        converted = []
        converted.append(headers)
        for row in data[1:2]:
            converted.append(convert(row))

        # Sort the columns on the input field
        sortedlist = sorted(converted, key=itemgetter(i), reverse=True)
    
    for player in sortedlist[0:10]:
        print(player[0], player[i])


    return

def search(player):
    headers = ['player', 'pos', 'age', 'tm', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', '3p', '3pa', '3p_pct', '2p', '2pa', '2p_pct', 'efg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'ps_per_g']
    with open("logs/nba_daily_stats.csv","r") as ifile:
        data = reader(ifile, delimiter=",")
        for p in data:
            if p[0].lower() == player.lower():
                print(", ".join(headers))
                print(", ".join(p))

def convert(row):
    print(row)
    new_row = []
    for v in row:
        try:
            v = float(v)
            new_row.append(v)
        except:
            new_row.append(v)
    print(new_row)
    return new_row
