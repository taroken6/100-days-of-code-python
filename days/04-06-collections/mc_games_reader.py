import csv
from collections import namedtuple, defaultdict

FILE_NAME = 'metacritic_games.csv'


def get_file():
    file = csv.DictReader(open(FILE_NAME, 'r'))
    return file


def list_game_by_developer(dict):
    for line in sorted(dict, key=lambda x: x['developer']):
        print(f'{line["developer"]:52}  {line["name"]}')


def list_game_by_score(dict):
    tmp = sorted(dict, key=lambda x: x['user_score'], reverse=True)
    tmp = sorted(tmp, key=lambda x: x['developer'].lower())
    for line in tmp:
        print(f'{line["developer"]:52}{line["user_score"]} {line["name"]}')


def run():
    dict = get_file()
    # list_game_by_developer(dict)
    list_game_by_score(dict)
