from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
from enum import Enum
import json
import sys
import time

class Kurse(Enum):
	Stufe1 = "70241"
	Stufe2a = "70242"
	Stufe2b = "70243"
	Stufe23 = "70244"
	Stufe3 = "70245"
	Spielkurs = "70246"

def getKursPostfix(day):
	return {
	"1" : Kurse.Stufe1.value,
	"2a" : Kurse.Stufe2a.value,
	"2b" : Kurse.Stufe2b.value,
	"23" : Kurse.Stufe23.value,
	"3" : Kurse.Stufe3.value,
	"Spielkurs" : Kurse.Spielkurs.value
	}.get(day, None)

### configures the driver by getting the executable etc.
def configureDriver():
	THISPATH = os.path.dirname(os.path.abspath(__file__))
	DRIVER_DIR = str(os.path.abspath(THISPATH + "/chromedriver"))

	#usr_input = "Mo/Spielkurs/Mi/Do/Sa/So: "
	#while usr_input not in [ "Mo", "Mi","Do", "Sa", "So", "Spielkurs"]:
	#    usr_input = input("Mo/Spielkurs/Mi/Do/Sa/So: ")
	#tag = usr_input

	# Start a new instance of the Chrome browser
	options = webdriver.ChromeOptions()
	options.headless = True
	driver = webdriver.Chrome(executable_path = DRIVER_DIR, options=options)
	return driver


### books the specified course
def bookCourse(driver):
	kursPrefix = "BS_Kursid_"
	buchenButtonPrefix = "BS_Termin_"

	day = ""
	if len(sys.argv) > 1 and getKursPostfix(sys.argv[1]) is not None:
		day = sys.argv[1]
	else: raise ValueError('argument not valid, valid arguments are: Mo/Spielkurs/Mi/Do/Sa/So')

	#load site
	driver.get("https://buchung.hochschulsport-hamburg.de/angebote/Wintersemester_2022_2023/_Volleyball.html")

	#select and click correct 'vormerken' button for kurs
	vormerken = driver.find_element("name", kursPrefix + getKursPostfix(day)).click()

	#go to new page
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	#select and click 'buchen' button
	driver.find_element("xpath", "/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input").click()
	#go to new page
	window_after = driver.window_handles[1]
	driver.switch_to.window(window_after)

	#execute javascript to show login window
	element = driver.find_element("id", "bs_pw_anmlink")
	driver.execute_script("arguments[0].click();", element)

	#load credentials.json
	email = ""
	password = ""
	with open('credentials.json') as json_file:
		data = json.load(json_file)
		for person in data["users"]:
			email = person["email"]
			password = person["pwd"]
			break

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


def sleep():
	### adds artificial slowdown to allow browser to handle request.
	time.sleep(3)

if __name__ == '__main__':
	driver = configureDriver()
	bookCourse(driver)
	driver.quit()
