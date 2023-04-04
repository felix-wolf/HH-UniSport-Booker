import datetime as dt
import time

def timeIsNow(time_to_book):
	# checks if now matches the time given in the json.
	# Script is run every 30 minutes, therefore we have a tolerance of 14 minutes.

	currentDayNum = dt.datetime.now().isoweekday()
	if (currentDayNum != int(time_to_book["day"])):
		return False

	# create datetime object of desired time
	desiredHour, desiredMinute = time_to_book["time"].split(":")
	desiredTime = dt.datetime.now()
	desiredTime = desiredTime.replace(hour = int(desiredHour), minute = int(desiredMinute))

	# calculate the difference between now and the desired time
	difference_in_minutes = abs((dt.datetime.now() - desiredTime).total_seconds() / 60)
	# return true if difference is less than 14 minutes
	if difference_in_minutes < 15:
		return True
	return False

def sleep():
	### adds artificial slowdown to allow browser to handle request.
	time.sleep(2)
