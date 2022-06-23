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
from fake_useragent import UserAgent
#
from time import sleep
#
#
# 
# ------------------> Logic of code <---------------------------


def configure_driver():
    """
    This funtion is to configure webdriver with necessary options.
    """

    # set driver;
    options = webdriver.FirefoxOptions()

    # declare the User-Agenr;
    user_agent = UserAgent()

    options.set_preference("general.useragent.override", user_agent.random)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Webdriver off = True, on = False;
    options.headles = False

    # set path to my webdriver;
    firefox_service = Service(executable_path=".../selenium-automation/geckodriver")
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver


# automation for ideisioferte.ro...
def move_in_site(driver):
    """ This function move in my entire site: ideisioferte.ro! """ 

    try: 
        driver.get('https://ideisioferte.ro')

        # find interviuri link;
        interviuri_link = driver.find_element(By.ID, 'menu-item-42').click()

        # target for scroll;
        target_1 = driver.find_element(By.ID, 'post-1344')
        driver.execute_script('arguments[0].scrollIntoView(true);', target_1)
        sleep(3)

        button_contact = driver.find_element(By.ID, 'menu-item-436').click()

        # target for new_message;
        target_2_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "wpforms-312-field_0")))
        driver.execute_script('arguments[0].scrollIntoView(true);', target_2_message)

        name_label = driver.find_element(By.ID, 'wpforms-312-field_0').send_keys("Andrei Cojocaru")
        sleep(1)
        email_label = driver.find_element(By.ID, 'wpforms-312-field_1').send_keys("andrei.reporter13@gmail.com")
        sleep(1)
        message_label = driver.find_element(By.ID, 'wpforms-312-field_2').send_keys("Acesta este un mesaj test trimis cu Python3, de la webautomation.ro!")
        sleep(1)
        acord_gdpr = driver.find_element(By.ID, 'wpforms-312-field_4_1').click()
        sleep(1)
        submit_button = driver.find_element(By.ID, 'wpforms-submit-312').click()

    except Exception as ex:
        print(ex)

    finally:
        sleep(15)
        driver.quit()



def main():
    
    driver = configure_driver()
    move_in_site(driver)


if __name__ == "__main__":
    main()

