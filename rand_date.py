from datetime import datetime
from random import randint

def random_datetime(start_date = datetime(2020, 1, 1, 0, 0 ,0), end_date = datetime(2024, 1, 1, 0, 0 ,0)):
    year = randint(int(start_date.strftime("%Y")), int((end_date.strftime("%Y"))))

    if year == int(start_date.strftime("%Y")):
        month = randint(int(start_date.strftime("%m")), 12)
    elif year == int(end_date.strftime("%Y")):
        month = randint(1, int(end_date.strftime("%m")))
    else:
        month = randint(1, 12)

    if year%4 == 0 and month == 2:
        day = randint(1, 29)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = randint(1, 30)
    elif month == 2:
        day = randint(1, 28)

    if year == int(start_date.strftime("%Y")) and month == int(start_date.strftime("%m")) and day == int(start_date.strftime("%d")):
        hour = randint(int(start_date.strftime("%H")), 23)
    elif year == int(end_date.strftime("%Y")) and month == int(end_date.strftime("%m")) and day == int(end_date.strftime("%d")):
        hour = randint(0, int(end_date.strftime("%H")))
    else:
        hour = randint(0, 23)

    if year == int(start_date.strftime("%Y")) and month == int(start_date.strftime("%m")) and day == int(start_date.strftime("%d")) and hour == int(start_date.strftime("%H")):
        minute = randint(int(start_date.strftime("%M")), 59)
    elif year == int(end_date.strftime("%Y")) and month == int(end_date.strftime("%m")) and day == int(end_date.strftime("%d")) and hour == int(end_date.strftime("%H")):
        minute = randint(0, int(end_date.strftime("%M")))
    else:
        minute = randint(0, 59)

    if year == int(start_date.strftime("%Y")) and month == int(start_date.strftime("%m")) and day == int(start_date.strftime("%d")) and hour == int(start_date.strftime("%H")) and minute == int(start_date.strftime("%M")):
        second = randint(int(start_date.strftime("%S")), 59)
    elif year == int(end_date.strftime("%Y")) and month == int(end_date.strftime("%m")) and day == int(end_date.strftime("%d")) and hour == int(end_date.strftime("%H")) and minute == int(end_date.strftime("%M")):
        second = randint(0, int(end_date.strftime("%S")))
    else:
        second = randint(0, 59)

    random_date = datetime(year, month, day, hour, minute, second)

    return random_date