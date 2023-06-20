from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import platform


# configures the driver by getting the executable etc.
def configureDriver():
    this_path = os.path.dirname(os.path.abspath(__file__))
    driver_dir = str(os.path.abspath(this_path + "/chromedriver"))

    # Start a new instance of the Chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    if platform.system() == "Linux":
        print("is linux")
        driver = webdriver.Chrome(executable_path=driver_dir, options=options)
        return driver
    elif platform.system() == "Darwin":
        print("is mac")
        driver = webdriver.Chrome(options=options)
        return driver
    return None
