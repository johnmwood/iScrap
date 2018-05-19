from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time 


def sleep_until_div(driver, div_id):
    """sleeps selenium web-driver until a div is found with the div_id present 
    
    having this function in a separate file abstracts out the functionality so it can be: 
        - used in multiple methods and classes 
        - separate out imports 
    """
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, div_id))
    )

    # wait for other divs to load inside courses
    time.sleep(2)
