from utils import sleep

def getCourseId(level):
	return {
	"1" : "70381",
	"23" : "70382",
	}.get(level, None)

### books the specified course
def bookCourse(level, driver):
	kursPrefix = "BS_Kursid_"
	buchenButtonPrefix = "BS_Termin_"

	#load site
	driver.get("https://buchung.hochschulsport-hamburg.de/angebote/Sommersemester_2023/_Floorball.html")

	print("site loaded")

	sleep()

	#select and click correct button for kurs
	vormerken = driver.find_element("name", kursPrefix + getCourseId(level)).click()

	sleep()

	return driver