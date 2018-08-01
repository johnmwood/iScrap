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

        # navigate to content tab from course home page 
        self.driver.find_element_by_link_text("Content").click()

        week_divs = self.get_week_divs()

        # loop through list of week's assignments
        for div in week_divs: 
            print(div) 

        ## create dictionary for each assignment 

        self.driver.quit()

    def get_week_divs(self): 
        pass 

    def scrap_data_by_week(self): 
        # yield weekly data 
        assignment = {
            "title": "", 
            "due_date": "", 
            "url": "", 
            "type": "", 
        }

        pass 
 


