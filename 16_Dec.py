#1
# print('Hello world, How are you?')
# print("Hello world, How are you?")
# print('''Hello world, How are you?''')
# print("""Hello world, How are you?""")
# print("""Hello world, How are you?\nI\'m Fine.""")

#2
# a="Hello world"
# print(a)
# print(a[0])
# print(a[1])
# print(a[-1])
# print(a[-2])
# print(a[0:5])
# print(a[:5])
# print(a[2:-2])
# for i in a:
#     print(i)

#3

# a = "Hello World."
# b = "Hello World, Prem Thakare."
# uncommon = ""

# for i in a:
#     if i not in b:
#         uncommon += i
# for j in b:
#     if j not in a:
#         uncommon += j

# print(uncommon)

#3.O

# a = input("Enter first : ").split(" ")
# b = input("Enter second : ").split(" ")

# for i in a:
#     if i not in b:
#         print(i)

# for i in b:
#     if i not in a:
#         print(i)


#4

# inpt = input("Enter the string : ")
# a = 0
# for i in inpt:
#     if(i not in ["0","1"]):
#         print("Not binary")
#         a = 1
#         break
# if(a==0):
#     print("Binary")

#5



#6

# str = input("Enter string : ")

# ind= int(input("Enter the index to be Removed:"))
# a= ""
# for i in range(0,len(str)):
#     if(i != ind):
#         a += str[i]

# print(a)

#7

class Employee:
    def getinfo(self):
        self.id = int(input("Enter the ID: "))
        self.name = input("Enter the Name: ")
        self.gender = input("Enter the Gender: ")
        self.city = input("Enter the City: ")
        self.salary = float(input("Enter the Salary: "))

    def display(self):
        print("\nID:", self.id)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("City:", self.city)
        print("Salary:", self.salary)

emp = Employee()

emp.getinfo()
emp.display()
