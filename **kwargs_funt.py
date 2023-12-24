'''kwargs'''

# def kbfunt(**kwargs):
#     print(kwargs)

# kbfunt(name="Prem",age=18)

''' unpack'''

# def kbfunt(**kwargs):
#     for i in kwargs:
#         print(i,"=",kwargs[i])

# kbfunt(name="Prem",age=18)

'''args and kwargs'''

# def kbfunt(*args,**kwargs):
#     print(args,kwargs)

# kbfunt(12,23,name="Prem",age=18)

''''Input'''

# def nam(a):
#     print("Welcome",a,",to ITM.")
# nam(a=input("What is your name:"))

'''input details Kwargs'''

# def stu(**kwargs):
#     for i in kwargs:
#         print(i,":",kwargs[i])
# stu(Name=input("What is your Name:"),Age=input("Your AGE:"),email=input("Enter your email address"))


'''input y and n'''
def stu(name,age,email):
    if (name=="y" and age=="n" and email=="n"):
        print(name)
    elif (name=="n" and age=="y" and email=="y"):
        print(age,email)
    elif (name=="y" and age=="y" and email=="n"):
        print(name,age)
name=input("What is your Name(y/n):")
age=int(input("Your AGE(y/n):"))
email=input("Enter your email address(y/n)")

stu(name,age,email)


