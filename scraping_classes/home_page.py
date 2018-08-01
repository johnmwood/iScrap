from scraper import Scraper 
from course import Course 
import threading
import re 


class Home_Page(Scraper): 
    """control selenium webdriver to scrap I-Learn for assignments"""
    def __init__(self): 
        super().__init__(starting_url="https://byui.brightspace.com/")

        self.course_data = self.get_course_data()

        self.driver.quit()

    def get_course_data(self):
        self.sleep_until_div(div_id="courses")
        current_semester_div = self.driver.find_element_by_xpath('//*[@id="courses"]/div/div[2]')

        # a list of course objects which will scrap their respective courses for data which will be used later 
        self.courses = [
            Course(name, div, url) 
            for name, div, url in self.find_course_names(current_semester_div)
        ]
        
        for course in self.courses:
            t = threading.Thread(target=course.scrap_course_data, args=())
            t.start()

    def find_course_names(self, semester_div):
        """yields every course name for every course div in the semester 

        makes an assumption that the last div is devotional (not a class) 
        and leaves the generator upon finding devotional 
        """
        i = 0 
        while True: 
            course_name = semester_div.find_element_by_xpath(f'div[{i+1}]/div[2]/div').get_attribute('innerHTML')
            course_div = semester_div.find_element_by_xpath(f'div[{i+1}]/div[2]')

            # the onclick attribute has a subtag in it which most likely makes sense to i-learn
            # the regex takes the subtag in the form "location.href='url'", and returns just the url 
            course_url = re.findall('^.*(https://byui.brightspace.com/d2l/home/[0-9]*)', course_div.get_attribute("onclick"))[0]

            if re.match('^Devotional', course_name): 
                return 

            i += 1
            yield course_name, course_div, course_url


if __name__ == "__main__": 
    ilearn_scraper = Home_Page()
