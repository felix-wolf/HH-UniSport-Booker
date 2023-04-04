from driver_configurator import configureDriver
from course_booker import bookCourse
from utils import timeIsNow
import os
import json

if __name__ == '__main__':
	print("start")
	driver = configureDriver()
	print("configured driver")

	#load credentials.json
	with open(os.path.dirname(os.path.abspath(__file__)) + '/bookings.json') as json_file:
		data = json.load(json_file)
		for entry in data:
			user = entry["user"]
			course = entry["course"]
			time_to_book = entry["timeToBook"]

			if timeIsNow(time_to_book):
				email = user["email"]
				password = user["password"]
				print("book course for user with email " + email)
				bookCourse(course["name"], course["level"], email, password, driver)
			else:
				print("time difference to large to book, return.")

	driver.quit()
	print("end")
