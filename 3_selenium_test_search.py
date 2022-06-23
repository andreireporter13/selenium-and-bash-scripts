#   New script for my QA portofolio; 
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
    """ This function configure webdriver! """

    # set driver;
    options = webdriver.FirefoxOptions()

    # declare a user agent;
    user_agent = UserAgent()

    options.set_preference("general.useragent.override", user_agent.random)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Webdriver off = True, on = False;
    options.headless = False

    # set path to firefox driver;
    firefox_service = Service(executable_path=".../selenium-automation/geckodriver")
    driver = webdriver.Firefox(service=firefox_service, options=options)

    return driver


# publi24 search function;
def publi24_search(driver, input_user_key_word) -> list:
    """ This functions make a search in google with keyword! """
    
    try:
        driver.get('https://publi24.ro')
        
        input_label = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "keyword"))).send_keys(input_user_key_word)
        button_search = driver.find_element(By.ID, 'btn-search').click()
        
        block_of_data = driver.find_elements(By.CLASS_NAME, 'large-8.medium-7.columns.article-title')

        for data in block_of_data:
            link = data.find_element(By.CLASS_NAME, 'maincolor').get_attribute('href')
            print(link)        

    except Exception as ex:
        print(ex)

    finally:
        sleep(5)
        driver.quit()


def main(): 
    """ This function is important - all code logic! """
    
    input_user_key_word = input('Introduceti un cuvant cheie pentru cautare pe publi24.ro: ')

    if input_user_key_word:
        driver = configure_driver()
        publi24_search(driver, input_user_key_word)
    else:   
        print('Something wrong')

    
    
if __name__ == "__main__":
    main()
