class Grandfather:
    def __init__(self):
        self.gfname = " Thakare"
        self.inheritance = 70000000

class Father(Grandfather):
    def __init__(self):
        super(Father, self).__init__()
        self.fname = input("Enter the Father Name: ") + self.gfname
        self.finheritance = float(input("Enter the Property purchased by Father: ")) + self.inheritance

class Child(Father):
    def __init__(self):
        super(Child, self).__init__()
        self.child = input("Enter the Child Name: ") + " " + self.fname
        self.cinheritance = float(input("Enter the Property purchased by " + self.child + " is: ")) + self.finheritance

c = Child()
print("\nHi,", c.child)
print("\nYour Total Assets is:\nInherited:", c.inheritance, "\nPurchased:", c.finheritance, "\nYour Property:", c.cinheritance)
