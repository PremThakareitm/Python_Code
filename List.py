l= []
n = int(input("Enter the Number of elements : "))
for i in range(0, n):  
    x =input()
    l.append(x) #append()	add an item to the end of the list
print(l)
print(l[0])
print(l[2:4])
print(len(l))

lst=["Rawlist",12,45,"lower"]
# add elements of even_numbers to the numbers list
# extend()	add all the items of an iterable to the end of the list
l.extend(lst)
print(l)
print(lst)
# insert an element at index 3 (fourth position)
# insert()	inserts an item at the specified index
lst.insert(3, 99)
print(l)
print(lst)

#Using del Statement
#Using remove()

#Check if an Element Exists in a List
lang = ['Prem', 'Thakare', 36]

print(6 in lang)    # False
print('Prem' in lang)    # True


# remove()	removes item present at the given index
lst.remove(12)
print(lst)
# pop()	returns and removes item present at the given index
lst.pop(2)
print(lst)

# clear()	removes all items from the list
# index()	returns the index of the first matched item
# count()	returns the count of the specified item in the list
print(l.count("prem"))

# sort()	sort the list in ascending/descending order
lo=["prem","anil","thakare"]
print(lo.sort())
# reverse()	reverses the item of the list
lst.reverse()
print(lst)
# copy()	returns the shallow copy of the list
lisa=lst.copy()
print(lisa)