#WAP List
# l=[10,20,30,40,50]
# print(l)

# for i in range(len(l)):
#     print(l[i])
# print(l.index(i))

# lst=["New Delhi","Mumbai","Pune","Nashik","New"]
# print(lst)
# print(lst[0:4])
#print(lst[0:-1])  

# lst.append("New")
# print(lst.pop(2))
# print(l.sort())

# lst.remove("New")
# print(lst)
# l.extend(lst)
# print(l)

# print(l.reverse())

# lst=[11,22,33,44,55,66]
# eve=[]
# print(lst)
# for i in lst:
#     if(i%2==0):
#         eve.append(i)
# print(eve)

#WAP

# l=[12,13,14,22,10]
# print(l[ : :-1])
# l.sort(reverse=True)
# print(l)

#WAP

# lst=["nashik","new"]
# z=l+lst
# print(z)

#WAP

# l=[23,45,10,2]
# sum=0
# for i in range(0,len(l)):
#     sum+=i
# print(sum)

#WAP to remove duplicate from list.

#WAP to Add two matrices in list.

l=[[23,34,10],[1,8,3],[12,6,5]]
b=[[1,5,6],[3,4,12],[23,0,11]]
addo=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(l)):
    for j in range(0,len(l[0])):
        addo[i][j]=l[i][j]+b[i][j]
print(addo)
