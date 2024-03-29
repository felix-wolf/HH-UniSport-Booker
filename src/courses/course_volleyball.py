from utils import sleep

def getCourseId(level):
	return {
	"1a" : "70346",
    "1b" : "72713",
	"2a" : "70351",
	"2b" : "70352",
	"23" : "70358",
	"3" : "70361",
	"Spielkurs" : "70365"
	}.get(level, None)

### books the specified course
def bookCourse(level, driver):
	kursPrefix = "BS_Kursid_"
	buchenButtonPrefix = "BS_Termin_"

	#load site
	driver.get("https://buchung.hochschulsport-hamburg.de/angebote/Sommersemester_2023/_Volleyball.html")

	print("site loaded")

	sleep()

	#select and click correct button for kurs
	vormerken = driver.find_element("name", kursPrefix + getCourseId(level)).click()

	sleep()

	return driver