import bank_module as balala

b = balala.Banking()
print("\nTotal Amount: Rs.", b.bala,"\n")
choice = int(input("Enter the Choice \n1.Withdraw\n2.Deposit\n3.Check Balance: "))

if choice == 1:
    withd = int(input("Enter the Amount to be Withdraw: "))
    b.operation(choice, withd, None) 
elif choice == 2:
    depo = int(input("Enter the Amount to be Deposit: "))
    b.operation(choice, None, depo)
elif choice == 3:
    b.operation(choice, None, None)
else:
    print("Invalid Input")