import datetime as dt
import time


def timeIsNow(time_to_book):
    # checks if now matches the time given in the json.
    # Script is run every 30 minutes, therefore we have a tolerance of 14 minutes.

    current_day_num = dt.datetime.now().isoweekday()
    if current_day_num != int(time_to_book["day"]):
        return False

    # create datetime object of desired time
    desired_hour, desired_minute = time_to_book["time"].split(":")
    desired_time = dt.datetime.now()
    desired_time = desired_time.replace(hour=int(desired_hour), minute=int(desired_minute))

    # calculate the difference between now and the desired time
    difference_in_minutes = abs((dt.datetime.now() - desired_time).total_seconds() / 60)
    # return true if difference is less than 14 minutes
    return difference_in_minutes < 15


def sleep():
    # adds artificial slowdown to allow browser to handle request.
    time.sleep(2)
