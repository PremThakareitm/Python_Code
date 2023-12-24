lts=[]
siz=int(input("Enter the number of elements:"))
for i in range(siz):
    x=int(input("Enter the Numbers: "))
    lts.append(x)
print("List of Numbers are:",lts)
sum=0
for i in lts:
    sum+=i
    avg=sum/siz
print("Sum of the Numbers:",sum)
print("Avg of the Numbers:",avg)