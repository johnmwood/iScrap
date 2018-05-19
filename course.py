class Course: 
    """this object will be instanciated for every course found in the user's I-Learn 

    Course will scrap the data and store it for TD 
    """
    def __init__(self, driver, name, div): 
        self.driver = driver 
        self.name = name 
        self.div = div 

        # fill dictionary with structured data from course 
        self.data = {} 

        self.scrap_course_data() 

    def scrap_course_data(self): 
        pass 

