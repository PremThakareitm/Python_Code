#WAP print all the letters of str1 than also apperingin str2.

def find(str1,str2):
    if(len(str1)>=len(str2)):
        for i in str1:
            if i in str2:
                print(i)

str1=input("Enter the first str1:")
str2=input("Enter the second str2:")
find(str1,str2)

#WAP to print the