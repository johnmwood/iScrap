# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import json 
import time


class Scraper: 
    """super class for all classes requiring selenium webdrivers to scrap i-learn

    e.g. Home_Page, Course 
    """
    def __init__(self, starting_url):
        self.login_page_title = "CAS – Central Authentication Service"

        with open('data/secret.json', 'r') as f:
            secret = json.load(f)

        self.login_credentials = {
            "username": secret.get("username"), 
            "password": secret.get("password"),
        }

        self.driver = webdriver.Firefox()
        self.driver.get(starting_url)

        # TODO: add more error handling to login 
        self.login()


    def login(self):
        # do not run without verifying page is for i-learn login 
        if self.driver.title == self.login_page_title:

            for key, value in self.login_credentials.items():
                field = self.driver.find_element_by_id(key)
                field.send_keys(value)

            submit_btn = self.driver.find_element_by_class_name("btn-login")
            submit_btn.click()

    def sleep_until_div(self, div_id):
        """sleeps selenium web-driver until a div is found with the desired div_id present"""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, div_id))
        )

        # wait for other divs to load inside courses
        time.sleep(2)
