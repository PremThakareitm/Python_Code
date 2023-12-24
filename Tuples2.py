# tpl=(1,3,42,12,42)

# print(tpl.count(42))
# print(tpl)
# into=int(input("Enter the number:"))
# if into in tpl:
#     print("Yes")
# else:
#     print("No")
    
# print(tpl.index(42,0,len(tpl)))

##WAP that scan the email address and form a tuple of username and domain.
n=int(input("Enter the Number of ID's: "))

dom=()
user=()
for i in range(n):
    tpl=input("Enter the email address: ")
    for i in range (0,len(tpl)):
        if(tpl[i]=="@"):
            dom=tpl[i:]
            user=tpl[:i]
    print("Username:",user)
    print("Domian:",dom)

