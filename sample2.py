import random

def greeting(name, age, email, roll):
    print("****")
    print(f"Welcome {name if name else 'Guest'} to ITM")
    
    if age is not None:
        print("Age:", age)
    
    if email is not None:
        print("Email:", email)
    
    print("Roll Number:", roll)
    print("****")

name_input = input("Do you want to give your name? ")
if name_input.lower() == 'yes':
    name = input("Enter your name: ")
else:
    name = None

age_input = input("Do you want to give your age? ")
if age_input.lower() == 'yes':
    age = int(input("Enter your age: "))
else:
    age = None

email_input = input("Do you want to enter your email? ")
if email_input.lower() == 'yes':
    email = input("Enter your email: ")
else:
    email = None

roll_number = random.randint(1001, 2000)

greeting(name, age, email, roll_number)