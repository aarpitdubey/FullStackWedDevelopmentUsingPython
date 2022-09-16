# 10. Write a python script to use IS operator to display if both variables are the same
# object or not?

class student:
    
    def __init__(self, name, course, isActive, Fee_paid, course_fee):
        
        self.name = name
        self.course= course
        self.isActive = isActive
        self.course_fee = course_fee
        self.Fee_paid = Fee_paid

s1 = student("Arpit Dubey", "Full stack Web Development using Python", True, 4000, True);   

def student_details():
    return name+" enrolled in "+course+" \n"+name+" Account is currently active: "+isActive+". \nIs course fee is paid: "+Fee_paid+"\nCourse fee is: "+course_fee

s1.student_details()