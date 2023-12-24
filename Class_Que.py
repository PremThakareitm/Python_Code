#WAP that has a class store which keeps the record of code and price of product 
#display the menu of all product and prompt his to enter the quantilty of each item required and 
#finally generate the bill  and display the total amount.

class Store:
    def __init__(self, product,code,price):
        self.product = product
        self.code = code
        self.price = price
    
    def getinfo(self):
        qty=0
        cho=input("Enter the Code:")
        if(cho=="A12"):
            qty=int(input("Enter the Quantity:"))
            
        
    def data(self):
        print("*----------------*\n|Code | Products |\n*----------------*\n|A12  | Cokes    |\n*----------------*\n|A13  | Sandwich |\n*----------------*")
