#MultiDimensional List
# l=[]
# n=int(input("Number of:"))
# for i in range(n):
#     x=input("values:")
#     l.append(x)
# l=[[1,3,6],[3,6,7],[1,"prem",9],[5,9,0]]
# print(l)
# print(l[2][2])
# print(len(l[2]))

# #List ke Ander List

# ls=[[23,4,5],[5,6,7],[8,9,l]]
# print(ls)
# print(ls[2][2][2][1])
# print(ls[2][2][2][1][3])

#WAP to find the smallest and largest element in the list

lop=[]
n=int(input("Number of Elements in List:"))

for i in range(n):
    x=int(input("Enter the Value of Elemets:"))
    lop.append(x)

max=lop[0]
min = lop[0]
for i in range (0,len(lop)):
    if(max<lop[i]):
        max=lop[i]
    elif(min>lop[i]):
        min=lop[i]     

print("Max Element:",max)
print("Min Element:",min)