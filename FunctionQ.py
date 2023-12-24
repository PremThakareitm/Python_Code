#WAP to get list in *args in tuple format an its sum.

l=[]
n=int(input("Enter the number of Elements:"))
for i in range(0,n):
    x=float(input("Enter the elements:"))
    l.append(x)

def funct(*args):
    sum=0.0
    for i in args:
        for i in l:
            sum=sum+i
        print("Sum:",sum)
funct(l)