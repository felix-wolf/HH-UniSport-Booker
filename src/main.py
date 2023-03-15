from driver_configurator import configureDriver
from courses.course_volleyball import bookCourse
import os
import json

if __name__ == '__main__':
	print("start")
	driver = configureDriver()
	print("configured driver")

	#load credentials.json
	with open(os.path.dirname(os.path.abspath(__file__)) + '/credentials.json') as json_file:
		data = json.load(json_file)
		for person in data["users"]:
			email = person["email"]
			password = person["pwd"]
			print("book course for user with email " + email)
			bookCourse(driver, email, password)

	driver.quit()
	print("end")
