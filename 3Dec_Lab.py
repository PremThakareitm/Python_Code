#WAP to add a tuple in a list
a=[1,3,5,6]
b=(67,46,78)
a.extend(b)
a+=b
print(a)

#WAP to find the lenght.
tup=(66,77,88,'car','roy',87.65)
print(len(tup))

#WAP list of tuple and its cube.

c=[2,4,5,6]
for i in c:
    c[i]=i**3
print(c)