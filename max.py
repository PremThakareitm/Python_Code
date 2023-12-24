num=[1,2,34,23]
max=num[0]
for i in range(0,len(num)):
    if(max<num[i]):
        max=num[i]
print(max)