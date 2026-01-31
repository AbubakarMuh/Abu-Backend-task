
'''
Question2:

Create a Python class student with attributes for name and age, and a method 
introduce that prints the student's details

'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def student_Details(self):
        print(f"Student is still under training session in TechVasity")

Student_Detail = Student("Abu_Laja", 40)

print(f"Student name is: {Student_Detail.name}")
print(f"Student age is: {Student_Detail.age}")
Student_Detail.student_Details()


# To run my code: python3 Python_Class_Assessment/student_Details.py