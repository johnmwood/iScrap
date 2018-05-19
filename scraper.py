from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from sleep_functions import sleep_until_div
from course import Course
import json 
import re 


class Scraper: 
    """control selenium webdriver to scrap I-Learn for assignments"""
    def __init__(self): 
        with open('data/secret.json', 'r') as f: 
            secret = json.load(f)

        self.login_credentials = {
            "username": "hooforfoo", 
            "password": secret.get("password")
        }
        self.url = "https://byui.brightspace.com/"
        self.login_page_title = "CAS – Central Authentication Service"

        self.init_driver()

    def init_driver(self): 
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

        # if session persists and login page is not loaded, do not attempt to login again 
        if self.driver.title == self.login_page_title: 
            self.login() 

        self.course_data = self.get_course_data()

    def login(self): 
        for key, value in self.login_credentials.items(): 
            field = self.driver.find_element_by_id(key)
            field.send_keys(value)

        submit_btn = self.driver.find_element_by_class_name("btn-login")
        submit_btn.click()

    def get_course_data(self):
        sleep_until_div(driver=self.driver, div_id="courses")
        current_semester_div = self.driver.find_element_by_xpath('//*[@id="courses"]/div/div[2]')

        # a list of course objects which will scrap their respective courses for data which will be used later 
        self.courses = [
            Course(self.driver, course_name, course_div) 
            for course_name, course_div in self.find_course_names(current_semester_div)
        ]
 
    def find_course_names(self, semester_div):
        """yields every course name for every course div in the semester 

        makes an assumption that the last div is devotional (not a class) 
        and leaves the generator upon finding devotional 
        """
        i = 0 
        while True: 
            course_name = semester_div.find_element_by_xpath(f'div[{i+1}]/div[2]/div').get_attribute('innerHTML') 
            course_div = semester_div.find_element_by_xpath(f'div[{i+1}]/div[2]')

            print(course_name)

            if re.match('^Devotional', course_name): 
                return 

            i += 1
            yield course_name, course_div 


if __name__ == "__main__": 
    ilearn_scraper = Scraper()
