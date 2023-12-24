# wap to count number of vowels in a given string considering both upper case and lower case.
# wap that takes a sentence as input and counts number of words in it.
# wap to check if two strings are anagrams of each other.
# wap that converts camel case string to snake case.
# wap that takes a list of strings as input and sorts them based on their length.


'''1'''
# a=input("Enter the String:")
# vowel = ["A","E","I","O","U"]
# count = 0

# for i in a:
#     if i.upper() in vowel:
#         count+=1
# print(count)

'''2'''
# a=input("Enter the String:")
# count=1
# for i in a:
#     if(i == " "):
#         count+= 1
# print(count)

'''3'''

# str1=input("Enter the String 1:")
# str2=input("Enter the String 2:")

# a=sorted(str1)
# b=sorted(str2)
# if(len(str1)==len(str2)):
#     if(a==b):
#         print("Anagram")
#     else:
#         print("Not anagram")
# else:
#     print("invalid")

'''4'''






'''5'''

lst=[]
n=int(input("Enter the Number of Elements:"))
for i in range(n):
    x=input("Enter the String:")
    lst.append(x)

j=(sorted(lst))
for i in j:
    y=len(i)
    z=sorted(y)
    print(z)
