#WAP to print first n natuaral number and their sum.

num=int(input("Enter the Nth number:"))
sum=0
for i in range(0,num+1):
    if(i>0):
        sum=i*(i+1)/2
print(sum)