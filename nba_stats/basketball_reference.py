#!/usr/bin/python
"""
Kicker for the Basketball Statistics Collector
"""

from datetime import datetime
import argparse
from functions.download import download
from functions.search import search, statistics

# Main parsing unit
parser = argparse.ArgumentParser(
    description='Basketball Statistics Collector, at your service!',
)

# create subparser for the commands
subparsers = parser.add_subparsers(help='Tasks to run', dest="command")

# Download command
dl_parser = subparsers.add_parser(
    'download', help='Download new CSV data')
dl_parser.add_argument('--year', action='store', default=False,
    help='Year to collect. By default the current season is used')

# Search command
search_parser = subparsers.add_parser(
    'search', help='Search data for certain player statistics')
search_parser.add_argument('--player', action='store', default=False,
    help='Search one player and print his statistics')
search_parser.add_argument('--statistic', action='store', default=False,
    help='Search top players in this category and print the list')
search_parser.add_argument('--statslist', action='store_true', default=False,
    help='Search top players in this category and print the list')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.command == 'download':
        if args.year:
            download(int(args.year))
        else:
            download()
    if args.command == 'search':
        if args.player:
            search(args.player)
        if args.statistic:
            statistics(args.statistic)
        if args.statslist:
            headers = ['player', 'pos', 'age', 'tm', 'g', 'gs', 'mp', 'fg', 'fga', 'fg_pct', '3p', '3pa', '3p_pct', '2p', '2pa', '2p_pct', 'efg_pct', 'ft', 'fta', 'ft_pct', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'ps_per_g']
            print(", ".join(headers))