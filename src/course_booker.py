from utils import sleep
from courses.course_volleyball import bookCourse as bookVolleyballCourse
from courses.course_floorball import bookCourse as bookFloorballCourse
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import datetime


def performBookingProcedure(driver, email, password):
    # go to new page
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    try:
        # select and click 'buchen' button
        book_button = driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div/div[2]/div[1]/label/div[2]/input")

        if book_button.get_attribute("value") != "buchen":
            print("No availability in course! Aborting...")
            return

        book_button.click()
    except NoSuchElementException:
        print("Buchen button not found.")
        return

    # go to new page
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)

    sleep()

    # execute javascript to show login window
    element = driver.find_element(By.ID, "bs_pw_anmlink")
    driver.execute_script("arguments[0].click();", element)

    sleep()

    # find and fill email field
    email_field = driver.find_element(By.NAME, "pw_email")
    email_field.send_keys(email)

    sleep()

    # find and fill password field
    password_field = driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[1]/div[3]/div[2]/input")
    password_field.send_keys(password)

    sleep()

    # find 'weiter zur Buchung' button and click it
    driver.find_element(By.XPATH, "/html/body/form/div/div[2]/div[1]/div[5]/div[1]/div[2]/input").click()

    sleep()

    # select checkbox 'AGB'
    driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[2]/label/input").click()

    sleep()

    # find and click 'weiter zur buchung' button
    driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[3]/div[2]/input").click()

    sleep()

    # find and click 'verbindlich buchen' button
    driver.find_element(By.XPATH, "/html/body/form/div/div[3]/div[1]/div[2]/input").click()

    sleep()

    driver.save_screenshot("screenshots/final_page" + "-" + email + "-" + str(datetime.datetime.now()) + ".png")

    if driver.find_element(By.LINK_TEXT, 'Ihre Buchung konnte nicht ausgeführt werden') is None:
        print("error :(")

    print("booked course")


def bookCourse(course_name, level, email, password, driver):
    if course_name == "volleyball":
        driver = bookVolleyballCourse(level, driver)
    elif course_name == "floorball":
        driver = bookFloorballCourse(level, driver)
    else:
        print("courseName not found")
        return
    performBookingProcedure(driver, email, password)
