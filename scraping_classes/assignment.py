from dataclasses import dataclass
import re 

"""
IMPORTANT: dataclass is only compatible verison >= Python 3.7 
"""
@dataclass
class Assignment:
    """class representing an assignment"""
    title: str
    due_date: str # datetime?
    url: str
    completed: bool = False

    def __post_init__(self):
        self.priority = self.is_ponder_and_prove()

    def is_ponder_and_prove(self):
        """ponder and prove assignments tend to be more important per week and represent more time effort than typical assignments
        for this reason, if the assignment is a ponder and prove, the priority of the task will be set higher

        the priority of a Todoist task can be 1-4, 1 being highest priority 
        """
        print(self.title)
        print()
        if re.match("ponder|Ponder", self.title):
            return 1
        else:
            return 4