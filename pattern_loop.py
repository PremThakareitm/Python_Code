num=int(input("Enter the Number of rows:"))

# for i in range(num+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print("\n")
    
# for i in range(num):
#     for j in range(0,num - i):
#         print("*" ,end=" ")
#     print("\n")
'''diamond'''
# for i in range(1, num + 1):
#         for j in range(num - i):
#             print(" ",end="")
        
#         for k in range(2 * i - 1):
#             print("*", end="")
        
#         print()

# for i in range(num, 0, -1):
#         for j in range(num - i):
#             print(" ", end="")

#         for k in range(2 * i - 1):
#             print("*", end="")
            
#         print()

'''hollow diamond'''

# Upper part of hollow diamond
for i in range(1, num+1):
    for j in range(1,(num-i)+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of hollow diamond
for i in range(num-1,0, -1):
    for j in range(1,num-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
