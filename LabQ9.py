#WAP to get the table of given number.

num=int(input("Enter a number:"))
rang=int(input("Enter a range:"))
step=int(input("Step:"))

# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
    

for i in range(1,rang+1,step):
    print(num,"*",i,"=",num*i)