#WAP that creates dictionary of cube of odd numbers in the range 1 to 10.

d={}
n=int(input("Enter the Range:"))
for i in range(0,n+1):
    if(i%2!=0):
        d[i]=i**3
print(d)