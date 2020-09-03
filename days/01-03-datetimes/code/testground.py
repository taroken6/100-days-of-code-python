from datetime import datetime
import os

with open('messages.log') as f:
    loglines = f.readlines()
tmp = [' '.join(x[-2:]) for x in loglines]
print(tmp)
res = [x for x in loglines if ' '.join(x[-2:]) == 'Shutdown initiated.']
print(res)

def run():
    line1 = 'ERROR 2014-07-03T23:24:31 supybot Invalid user dictionary file'
    line2 = 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    line3 = 'INFO 2016-09-03T02:11:22 supybot Shutdown complete.'

    # print(convert_to_datetime(line1))
    # print(convert_to_datetime(line2))
    # print(convert_to_datetime(line3))



def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    datetime_string = line.split()[1]  # ex: 'INFO 2015-10-03T10:12:51 supybot Shutdown initiated.'
    datetime_object = datetime.strptime(datetime_string, '%Y-%m-%dT%H:%M:%S')
    return datetime_object


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """

