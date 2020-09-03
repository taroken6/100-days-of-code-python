# Day 3 Project
import datetime


def run():
    inp = ''
    while inp.lower() != 'y':
        inp = input('Start stopwatch? Y/N: ')
    start = datetime.datetime.now()

    inp = ''
    while inp.lower() != 'y':
        inp = input('Stop stopwatch? Y/N: ')
    end = datetime.datetime.now()
    tdelta = end - start
    seconds = tdelta.seconds
    mseconds = tdelta.microseconds
    print(f'{seconds}.{mseconds}')
