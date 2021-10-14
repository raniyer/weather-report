import pytz
from datetime import datetime

def gmt_to_calcutta(unix_gmt):
    calcutta = pytz.timezone('Asia/Calcutta')
    gmt = pytz.timezone('GMT')
    date = datetime.utcfromtimestamp(unix_gmt)
    date = gmt.localize(date)
    calcutta_time = date.astimezone(calcutta)
    return calcutta_time

if __name__ == '__main__':
    for timezone in pytz.all_timezone:
        print(timezone)