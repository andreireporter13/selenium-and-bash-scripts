#   New script for my QA portofolio; 
#
#   Author: Andrei Cojocaru
#   LinkedIn: https://www.linkedin.com/in/andrei-cojocaru-985932204/
#   Twitter: https://twitter.com/andrei_reporter
#   Website: https://ideisioferte.ro && https://webautomation.ro
#   Project date-time: 
#
#################################################################################
#
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#
import requests
#
from fake_useragent import UserAgent
#
from time import sleep
#
#
# 
# ------------------> Logic of code <---------------------------

def configure_driver():
    """ This function is configure webdriver! """

    # set driver;
    options = webdriver.FirefoxOptions()

    # declare the User-Agenr;
    user_agent = UserAgent()


    options.set_preference("general.useragent.override", user_agent.random)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Webdriver off = True, on = False;
    options.headless = False

    # set path to my webdriver;
    firefox_service = Service(executable_path=".../selenium-automation/geckodriver")
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver
    

# get requests for webautomation.ro;
def webautomation_get_request():

    response = requests.get('https://webautomation.ro')

    return response


def main():
    """ This function is important - is all logic! """

    if webautomation_get_request() == 200:
        print(f'The site response is: {webautomation_get_request()}')
        driver = configure_driver()
        driver.get('https://webautomation.ro')

    else:
        print(f'The site response is: {webautomation_get_request()}')
        driver = configure_driver()
        driver.get('https://webautomation.ro')

    sleep(5)

    driver.quit()


if __name__ == "__main__":
    main()
