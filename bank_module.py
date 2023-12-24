class Banking:
    def __init__(self):
        self.bala = 70000

    def operation(self, choice, withd, depo):
        if (choice == 1):
            if withd <= self.bala:
                self.bala -= withd
                print("\nTotal Amount: Rs.", self.bala)
            else:
                print("Insufficient Balance to Withdraw")
        elif (choice == 2):
            self.bala += depo
            print("\nTotal Amount: Rs.", self.bala)
        elif (choice == 3):
            print("\nTotal Amount: Rs.", self.bala)
        else:
            print("Invalid Input")