from datetime import datetime, timedelta
from random import randint

def random_datetime(start_date = datetime(2020, 1, 1, 0, 0 ,0), end_date = datetime(2024, 1, 1, 0, 0, 0)):
    total_time_diff = (end_date - start_date)
    rand_day = randint(0, total_time_diff.days)

    if rand_day == total_time_diff.days:
        random_date = (start_date + timedelta(days=randint(0, total_time_diff.days), seconds=randint(0, total_time_diff.seconds)))
    else:
        random_date = (start_date + timedelta(days=randint(0, total_time_diff.days), seconds=randint(0, 86400)))

    return random_date