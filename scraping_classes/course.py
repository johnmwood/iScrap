from assignment import Assignment
from scraper import Scraper 


class Course(Scraper): 
    """this object will be instanciated for every course found in the user's I-Learn 

    Course will scrap the data and store it for TD 
    """
    def __init__(self, name, div, url): 
        self.url = url 
        self.name = name 
        self.div = div 

        # fill dictionary with structured data from course 
        self.data = {} 

    def scrap_course_data(self):
        # intanciate web driver from scraper and login
        super().__init__(starting_url=self.url)

        # all courses have overlayContent divs for the course photo
        # do not attempt any operations without first loading the page
        self.sleep_until_div("overlayContent")

        # navigate to content tab from course home page 
        self.driver.find_element_by_link_text("Content").click()

        week_divs = self.get_weekly_divs()

        # loop through list of week's assignments
        # for div in week_divs: 
        #     print(div) 

        ## create dictionary for each assignment 

        self.driver.quit()

    def get_weekly_divs(self): 
        table_of_contents_div = self.driver.find_elements_by_class_name("d2l_two_panel_selector_main")
        print(table_of_contents_div)
        
        
        # i = 0 
        # while True: 
        #     # start at the third div because table of contents doesn't have assignments 
        #     tree.find_element_by_xpath(f"div[{i+2}]/div/div/div/div/")

    def scrap_data_by_week(self): 
        # yield weekly data 
        assignment = {
            "title": "", 
            "due_date": "", 
            "url": "", 
            "type": "", 
        }

        pass 
 


