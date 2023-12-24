#WAP to find the Greatest of 3 numbers.

a=float(input("Enter the First number:"))
b=float(input("Enter the Second number:"))
c=float(input("Enter the Third number:"))

if(a>=b and a>=c):
    print(a,"is Greater")
elif(b>=c and b>=a):
    print(b,"is Greater")
elif(c>=a and c>=b):
    print(c,"is Greater")
else:
    print("Enter the Valid input")