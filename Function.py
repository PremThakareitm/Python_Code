# def sum(a,b):
#     print("Sum",a+b)

# def sub(a,b):
#     print("Sub",a-b)
    
# def mult(a,b):
#     print("Mult",a*b)

# def div(a,b):
#     print("Div",a/b)
    
# def power(a,b):
#     print("Power",a**b)
    
# def remi(a,b):
#     print("Remi",a%b)
    
# def flodevi(a,b):
#     print("Flodevi",a//b)

# a=int(input("Enter the First Number:"))
# b=float(input("Enter the Second Number:"))
# sum(a,b)
# sub(a,b)
# mult(a,b)
# div(a,b)
# power(a,b)
# remi(a,b)
# flodevi(a,b)

#WAP to calculate square root and .
# import math
# def square(num):
#     print("Square root of",num,"is:",num**2)
#     print("Under root of",num, "is:",math.sqrt(num))
# num=int(input("Enter the Number:"))
# square(num)

#WAP to Pass multiple arguments.

# def my_fun(*args):
#     for i in args:
#         print(i)
#     print(args)
# my_fun(1,2)
# my_fun(11,3)

#WAP to add the Arguments.

def my_fun(*args):
    sum=0
    for i in args:
        sum=sum+i
    print("Sum:",sum)
my_fun(float(input("Enter the First Number:")))
my_fun(float(input("Enter the Second Number:")))

