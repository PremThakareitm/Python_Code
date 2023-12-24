# ask=int(input("Enter what you want to learn 1. Arthematic use, 2. Indentity use. "))
# if ask==1:
#     print("_____Arthematic opertor____")
#     a=int(input("Enter first number: ") )
#     b=int(input("Enther secound number: "))
#     choice=int(input("Enter the calculation you want to perform 1 for Addition, 2 for substraction, 3 for multiplication and 4 for division. "))

#     if choice<=4:
#         def case1():
#             print(a+b)
#         def case2():
#             print(a-b)
#         def case3():
#             print(a*b)
#         def case4():
#             print(a/b)

#         def switch_case(case):

#             if(case == 1):
#                 case1()
#             elif(case == 2):
#                 case2()
#             elif(case == 3):
#                 case3()
#             elif(case == 4):
#                 case4()
            
        
#         switch_case(choice)
#     else:
#         print("Enter number between 1 to 5... Please! ")

# elif ask==2:
#     print("____Use of Identity operators___")
#     print("TO understand its use simply enter 1 to 5 numbers. ")
#     list = []
#     inputs=[1,2,3,4,5]
#     a=5

#     while(not(a==0)):
#         a = input("Enter an element for the list (or 'done' to finish): ")
#         if(not(a == 0)):
#             l.append(a)

#         if a.lower() == 'done':
#             break   
    
#         list.append(a)

#         if list is inputs :
#             print("Correct, Simply the list of 1 to 5 number was already available in code it just checked that data was matching to user input which simply used identity operator")
#         elif list is not inputs: 
#             print("Wrong inputs of number 1 to 5.... and the already predefined data was not matching with user input and for checking condition the indentity operator was used .")

# j="prem"
# a=1+3j
# print(type(j))

def my_fun():
    return("Prem Thakare")
my_fun()
sto=my_fun()
print(type(my_fun))