#WAP o check the given year is leap year.

y=int(input("Enter the Year:"))

if((y%4==0 and y%100!=0) or (y%400==0)):
    print("The year",y,"is leap year.")
else:
    print("The year",y,"is not a leap year.")