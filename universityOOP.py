class Person:
    def __init__(self, name="", age=0, gender=""):
        self.name = name
        self.age = age
        self.gender = gender
   
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
   
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"



class Student(Person):
    def __init__(self, name="", age=0, gender="", student_id="", course=""):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.grades = []
   
    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
   
    def add_grade(self, grade):
        self.grades.append(grade)
   
    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0
   
    def get_student_summary(self):
        avg_grade = self.calculate_average_grade()
        return f"{self.get_details()}, Student ID: {self.student_id}, Course: {self.course}, Average Grade: {avg_grade:.2f}"
    
    def get_mentor(self,professor):
        return 'No mentor assigned'


class Professor(Person):
    def __init__(self, name="", age=0, gender="", staff_id="", department="", salary=0):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
   
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
   
    def give_feedback(self, student, feedback):
        print(f"Feedback for {student.name}: {feedback}")
   
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)
   
    def get_professor_summary(self):
        return f"{self.get_details()}, Staff ID: {self.staff_id}, Department: {self.department}, Salary: £{self.salary}"
    
    def mentor_student(self,student):
        print(f'professor{self.name} is now mentoring student{student.name} on {student.course}')

class Administrator(Person):
    def __init__(self, name="", age=0, gender="", admin_id="", office="", years_of_service=0):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
   
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
   
    def increment_service_years(self):
        self.years_of_service += 1
   
    def get_admin_summary(self):
        return f"{self.get_details()}, Admin ID: {self.admin_id}, Office: {self.office}, Years of Service: {self.years_of_service}"


student1 = Student()
student1.set_details("Hamim Ahnaf", 17, "Male")
student1.set_student_details("S5678", "Physics")
student1.add_grade(85)
student1.add_grade(90)

student2 = Student()
student2.set_details("Hamza Rahman", 36, "Male")
student2.set_student_details("S1234", "Engineering")
student2.add_grade(78)
student2.add_grade(82)


professor1 = Professor()
professor1.set_details("Mr Rakib", 45, "Male")
professor1.set_professor_details("P1234", "Chemistry", 50000)

professor2 = Professor()
professor2.set_details("Mr Reynolds", 65, "Female")
professor2.set_professor_details("P5678", "English", 30000)


admin = Administrator()
admin.set_details("Ms Begum", 40, "Female")
admin.set_admin_details("A4321", "Room G12, Head of year office", 8)


print(student1.get_student_summary())  
print(student2.get_student_summary())  

professor1.give_feedback(student1, "Great work on your assignment!") 
professor2.give_feedback(student2, "Good effort, but could improve.") 

professor1.increase_salary(10) 
professor2.increase_salary(1)  

admin.increment_service_years()  


print(professor1.get_professor_summary()) 
print(professor2.get_professor_summary()) 
print(admin.get_admin_summary()) 