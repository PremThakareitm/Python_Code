# Slicing the string

str="PREM ANIL THAKARE"
print(str[::-1])
print(str[0:3:2])
print(str[-1:-5:-3])
print(str[0:5]+str[10:])

for i in str:
    print(i)
    
i=0
while i<len(str):
    print(str[i])
    i+=1
    

