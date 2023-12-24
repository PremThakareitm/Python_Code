'''l= []
n = int(input("Enter the Number of elements : "))
for i in range(0, n):  
    x = int(input())
    l.append(x) 
ch=input("Enter the Operation you wish to perform:\n1.Arithmetic\n2.Comparing the Elements")
if(ch==1):
    input("Enter the Arithmetic Operations(+,-,*,/,power):")
    if(ch=="+"):
        
        
    elif(ch=="-"):
        print("Sum of", a, "-", b,"=",a-b)
    elif(ch=="-"):
        print("Sum of", a, "*", b,"=",a*b)
    else:
        print("Sum of", a, "/", b,"=",a/b) '''
        
ch=int(input("Enter the Operation you want to perform:\n1.Arithmetic\n2.Comparing the Elements\n3.Get the List of Elements\n" ))
if(ch==1):
    x=input("Arithmetic Operations\n +,-,*,/,power:")
    a=float(input("Enter the First Number"))
    b=float(input("Enter the Second Number"))
    if(x=="+"):
        print("Sum of",a,"+",b,"is",a+b)
    elif(x=="-"):
        print("Difference of",a,"-",b,"is",a-b)
    elif(x=="*"):
        print("Multipling",a,"*",b,"is",a*b)
    elif(x=="/"):
        print("Division of",a,"/",b,"is",a/b)
    else:
        print(a,"to the power",b,"is",a**b)
elif(ch==2):
    a=float(input("Enter the First Number"))
    b=float(input("Enter the Second Number"))
    if(a>b and b<a):
        print(a,"is greater")
    elif(b>a and a<b):
        print(b,"is greater")
    else:
        print("Both numbers are Equal")
else:
    l= []
    n = int(input("Enter the Number of elements : "))
    for i in range(0, n):  
        x = int(input())
        l.append(x)
    ind=input("Enter the number:")
    print(ind in l)
