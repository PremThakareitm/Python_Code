
# for i in range(0,3):
#     asc=65

#     for j in range(0,i):
#         print(" ",end="")

#     for j in range(i,5):
#         print(chr(asc+j),end=" ")
#     print("")
''''''
# for i in range(2,0 , -1):
#     asc1 = 65+i
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(0,5-i):
#         print(chr(asc1+j),end=" ")
#     print("")


# for i in range (0,3):
#     asc=65
#     for j in range(0,i):
#         print(" ",end="")
#     for j in range(i,5):
#         print(chr(asc+j),end=" ")
#     print("")

''' '''

for i in range(1, 5):
    for j in range(i,4):
        print(" ", end="")
    
    for j in range(1, i):
        if(j == i-1):
            print("*",end="")
            continue
        print("* ", end="")
    
    for j in range(i, 5):
        if(j == 4):
            print(" ",end="")
            continue
        print("  ", end="")
        
    
    for j in range(1,i):
        
        print("* ", end="")
    
    print()