# class student:
#     count=0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("name:",self.name,"\nAge:",self.age)
# obj=student("Prem",18)
# obj.display()

# # WAP to admission of students

# class Admit:
#     def __init__(self):
#         self.lst = []

#     def getinfo(self):
#         n = int(input("Enter the Number of Students: "))
#         for i in range(n):
#             x = input("Enter the Name of the Student: ")
#             y = int(input("Enter the Age of the Student: "))
#             z = input("Enter the Department of the Student:")
#             self.lst.append((x, y, z))

#     def display(self):
#         print("Students Details:\n", self.lst)

# obj = Admit()
# obj.getinfo()
# obj.display()

# Sort by Department:

# class Admit:
#     def __init__(self):
#         self.lst = []

#     def getinfo(self):
#         n = int(input("Enter the Number of Students: "))
#         for i in range(n):
#             x = input("Enter the Name of the Student: ")
#             y = int(input("Enter the Age of the Student: "))
#             z = input("Enter the Department of the Student:")
#             self.lst.append((x, y, z))

#     def display(self):
#         print("Students Details:\n", self.lst)
        

# obj = Admit()
# obj.getinfo()
# obj.display()

#WAP to admit the students in the different Departments(pgdm/btech) and count the students 

class ITM:
    count = 0
    def get(self):
        self.name = input("Enter the name of the student: ")
        self.age = int(input("Enter the age: "))
        self.dep = int(input("Enter the department (1 for B.Tech, 2 for PGDM): "))
        ITM.count += 1

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        if self.dep == 1:
            print("Department: B.Tech")
        elif self.dep == 2:
            print("Department: PGDM")
        print()


students = int(input("Enter the number of students: "))

btech_students = []
pgdm_students = []

for i in range(students):
    student = ITM()
    student.get()
    
    if student.dep == 1:
        btech_students.append(student)
    elif student.dep == 2:
        pgdm_students.append(student)

print("\nB.Tech Students:")
for student in btech_students:
    student.display()

print("\nPGDM Students:")
for student in pgdm_students:
    student.display()

print("\nTotal Admissions:", ITM.count)