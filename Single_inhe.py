# class Parent:
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         return self.a + self.b

# class Child(Parent):
#     def takevalues(self):
#         x = float(input("Enter the first value: "))
#         y = float(input("Enter the second value: "))
#         c = self.add(x, y)
#         print("Sum of",x,"+",y," is :", c)

# obj = Child()
# obj.takevalues()

###
# class Shape:
#     def rect(self):
#         print("\nArea of Rectangle is:",self.l * self.b,"\n")

# class Area(Shape):
#     def takevalues(self):
#         self.l = float(input("\nEnter the Lenght value: "))
#         self.b = float(input("Enter the Width value: "))

# obj = Area()
# obj.takevalues()
# obj.rect()

# class Shape:
#     def rect(self,l,b):
#         print("\nArea of Rectangle is:",self.l * self.b,"\n")

# class Area(Shape):
#     def takevalues(self):
#         self.l = float(input("\nEnter the Lenght value: "))
#         self.b = float(input("Enter the Width value: "))

# obj = Area()
# obj.takevalues()
# obj.rect(obj.l,obj.b)

################################################################

# class Area:
#     def area(self,l1=None,l2=None,l3=None):
#         if (self.l1 != None and self.l2 == None and self.l3 == None):
#             print("\nArea of Square is:",self.l1 * self.l1,"\n")
#         elif (self.l1 != None and self.l2 != None and self.l3 == None):
#             print("\nArea of Rectangle is:",self.l1 * self.l2,"\n")
#         elif(self.l1 != None and self.l2 != None and self.l3 != None):
#             print("\nArea of Cuboid  is:",self.l3 * self.l1 * self.l2,"\n")
        
# class Side(Area):
#     def takevalues(self):
#         cho=int(input("\nEnter the Operation to be performed:\n1.Area of SQUARE\n2.Area of RECTANGLE\n3.Area of CUBOID\n:"))
#         if (cho==1):
#             self.l1=int(input("Enter the Side of Square:"))
#             self.l2=None
#             self.l3=None
#         elif (cho==2):
#             self.l1=int(input("Enter the Lenght of Rectangle:"))
#             self.l2=int(input("Enter the Width of Rectangle:"))
#             self.l3=None
#         elif (cho==3):
#             self.l1=int(input("Enter the Lenght of Cuboid:"))
#             self.l2=int(input("Enter the Width of Cuboid:"))
#             self.l3=int(input("Enter the Height of Cuboid:"))
#         else:
#             print("Please enter Valid Options...")

# obj = Side()
# obj.takevalues()
# obj.area()


