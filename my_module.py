print("Module name of my_module is:",__name__)

class Addititon:
    def add(self,x,y):
        print(x+y)

class Subtraction:
    def sub(self,x,y):
        print(x-y)
if __name__ == '__main__':
    print("Executed Directly")
else:
    print("Executed after import")    

# class Division:
#     def divide(self,x,y):
#         print(x/y)

# class multiplication:
#     def mul(self,x,y):
#         print(x*y)

# class Modulus:
#     def mod(self,x,y):
#         print(x%y)



