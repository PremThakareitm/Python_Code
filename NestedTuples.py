#WAP to print the name of a topper and his/her marks in four subject wherein
#marks are specified as a list in a tuple named topper(nested tuples)


stu = []
for i in range(4):
    n= input("Enter name of student: ")
    marks=int(input("Enter marks for in four subjects: ").split())
    data=(n,marks)
    stu.append(data)
print(stu)


