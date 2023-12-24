#WAP Arithmetic Operations and perform operation

a=float(input("Enter the First Number:"))
b=float(input("Enter the Second Number:"))

d=input("Enter the Arithmetic Operations\n(+,-,*,/,//,%,power):")
if(d=="+"):
    print("Sum of", a, "+", b,"=",a+b)
elif(d=="-"):
    print("Sub of", a, "-", b,"=",a-b)
elif(d=="*"):
    print("Multiplication of", a, "*", b,"=",a*b)
elif(d=="/"):
    print("Division of", a, "/", b,"=",a/b)
elif(d=="//"):
    print("Floor Division of",a,"//",b,"is:",a//b)
elif(d=="%"):
    print("Reminder of",a,"%",b,"is:",a%b)
else:
    print(a,"to the power of", b,"is:",a**b)
    