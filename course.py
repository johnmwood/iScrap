from selenium import webdriver


class Course: 
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
        print("let's see what happens")
        driver = webdriver.Firefox()
        driver.get(self.url)

        driver.quit()



