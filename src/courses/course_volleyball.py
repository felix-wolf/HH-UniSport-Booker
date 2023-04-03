from enum import Enum
import json
import sys
import time
import platform

class Kurse(Enum):
	Stufe1a = "70346"
    Stufe1b = "72713"
	Stufe2a = "70351"
	Stufe2b = "70352"
	Stufe23 = "70358"
	Stufe3 = "70361"
	Spielkurs = "70365"

def getKursPostfix(day):
	return {
	"1a" : Kurse.Stufe1a.value,
    "1b" : Kurse.Stufe1b.value,
	"2a" : Kurse.Stufe2a.value,
	"2b" : Kurse.Stufe2b.value,
	"23" : Kurse.Stufe23.value,
	"3" : Kurse.Stufe3.value,
	"Spielkurs" : Kurse.Spielkurs.value
	}.get(day, None)

### books the specified course
def bookCourse(driver, email, password):
	kursPrefix = "BS_Kursid_"
	buchenButtonPrefix = "BS_Termin_"

	day = ""
	if len(sys.argv) > 1 and getKursPostfix(sys.argv[1]) is not None:
		day = sys.argv[1]
	else: raise ValueError('argument not valid, valid arguments are: 1a/1b/2a/2b/23/3/Spielkurs')

	print("cli argument was valid")

	#load site
	driver.get("https://buchung.hochschulsport-hamburg.de/angebote/Sommersemester_2023/_Volleyball.html")

	print("site loaded")

	sleep()

	#select and click correct button for kurs
	vormerken = driver.find_element("name", kursPrefix + getKursPostfix(day)).click()

	sleep()

	#go to new page
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	#select and click 'buchen' button
	buchenButton = driver.find_element("xpath", "/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input")

	if buchenButton.get_attribute("value") != "buchen":
		print("No availability in course! Aborting...")
		return

	buchenButton.click()
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

	driver.save_screenshot('login.png')

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

	driver.save_screenshot('final_page.png')
	print("booked course")

def sleep():
	### adds artificial slowdown to allow browser to handle request.
	time.sleep(2)
