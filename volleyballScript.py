from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from enum import Enum
import datetime
import json

class Kurse(Enum):
	Montag = "48098"
	Mittwoch = "48092"
	Donnerstag = "48095"
	Samstag = "48096"
	Sonntag = "48097"
	Spielkurs = "48101"

def getKursPostfix(tag):
	return {
	"Mo" : Kurse.Montag.value,
	"Mi" : Kurse.Mittwoch.value,
	"Do" : Kurse.Donnerstag.value,
	"Sa" : Kurse.Samstag.value,
	"So" : Kurse.Sonntag.value,
	"Spielkurs" : Kurse.Spielkurs.value
	}[tag]

kursPrefix = "BS_Kursid_"
buchenButtonPrefix = "BS_Termin_"
THISPATH = os.path.dirname(os.path.abspath(__file__))
DRIVER_DIR = os.path.abspath(THISPATH + "/chromedriver")

usr_input = "Mo/Spielkurs/Mi/Do/Sa/So/: "
while usr_input not in [ "Mo", "Mi","Do", "Sa", "So", "Spielkurs"]:
    usr_input = input("Mo/Spielkurs/Mi/Do/Sa/So/: ")

#load site
driver = webdriver.Chrome(executable_path = DRIVER_DIR)
driver.get("https://buchung.hochschulsport-hamburg.de/angebote/Wintersemester_2019_2020/_Volleyball.html")
#select and click correct 'vormerken' button for kurs
vormerken = driver.find_element_by_name(kursPrefix + getKursPostfix(usr_input)).click()
#go to new page
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
#select and click 'buchen' button
driver.find_element_by_xpath("/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input").click()
#go to new page
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
#execute javascript to show login window
element = driver.find_element_by_id("bs_pw_anmlink")
driver.execute_script("arguments[0].click();", element)
#load credentials.json
email = ""
password = ""
with open('credentials.json') as json_file:
	data = json.load(json_file)
	for person in data["people"]:
		email = person["credentials"]["email"]
		password = person["credentials"]["pwd"]
		break
#find and fill email field
emailField = driver.find_element_by_name("pw_email")
emailField.send_keys(email)
#find and fill password field
passwordField = driver.find_element_by_xpath("/html/body/form/div/div[2]/div[1]/div[3]/div[2]/input")
passwordField.send_keys(password)
#find 'weiter zur Buchung' button and click it
driver.find_element_by_xpath("/html/body/form/div/div[2]/div[1]/div[5]/div[1]/div[2]/input").click()
#select checkbox 'AGB'
driver.find_element_by_xpath("/html/body/form/div/div[3]/div[2]/label/input").click()
#find and click 'weiter zur buchung' button
driver.find_element_by_xpath("/html/body/form/div/div[3]/div[3]/div[2]/input").click()
#find and click 'verbindlich buchen' button 
driver.find_element_by_xpath("/html/body/form/div/div[3]/div[1]/div[2]/input").click()




