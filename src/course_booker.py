from utils import sleep
from courses.course_volleyball import bookCourse as bookVolleyballCourse
from courses.course_floorball import bookCourse as bookFloorballCourse
import datetime

def performBookingProcedure(driver, email, password):
	#go to new page
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	try:
		#select and click 'buchen' button
		buchenButton = driver.find_element("xpath", "/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input")

		if buchenButton.get_attribute("value") != "buchen":
			print("No availability in course! Aborting...")
			return

		buchenButton.click()
	except:
		print("Buchen button not found.")
		return

	#go to new page
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	sleep()

	#execute javascript to show login window
	element = driver.find_element("id", "bs_pw_anmlink")
	driver.execute_script("arguments[0].click();", element)

	sleep()

	#find and fill email field
	emailField = driver.find_element("name", "pw_email")
	emailField.send_keys(email)

	sleep()

	#find and fill password field
	passwordField = driver.find_element("xpath", "/html/body/form/div/div[2]/div[1]/div[3]/div[2]/input")
	passwordField.send_keys(password)

	sleep()

	#find 'weiter zur Buchung' button and click it
	driver.find_element("xpath", "/html/body/form/div/div[2]/div[1]/div[5]/div[1]/div[2]/input").click()

	sleep()

	#select checkbox 'AGB'
	driver.find_element("xpath", "/html/body/form/div/div[3]/div[2]/label/input").click()

	sleep()

	#find and click 'weiter zur buchung' button
	driver.find_element("xpath", "/html/body/form/div/div[3]/div[3]/div[2]/input").click()

	sleep()

	#find and click 'verbindlich buchen' button
	driver.find_element("xpath", "/html/body/form/div/div[3]/div[1]/div[2]/input").click()

	sleep()

	driver.save_screenshot("screenshots/final_page" + "-" + email + "-" + str(datetime.datetime.now()) + ".png")

	print("booked course")


def bookCourse(courseName, level, email, password, driver):
	if courseName == "volleyball":
		driver = bookVolleyballCourse(level, driver)
	elif courseName == "floorball":
		driver = bookFloorballCourse(level, driver)
	else:
		print("courseName not found")
		return

	performBookingProcedure(driver, email, password)