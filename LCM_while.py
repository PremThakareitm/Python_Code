#WAP to find LCM of two numbers.

num1 = int(input("Number1:"))
num2 = int(input("Number2:"))
if(num1 > num2 ):
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break
    max= max+ 1