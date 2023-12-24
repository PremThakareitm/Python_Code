#WAP TO UNPACK A TUPLE IN SERVAL VARIABLES.

# tpl=(12,32,91)
# a,b,c=tpl
# print(a)

#WAP to remove empty tuples from a list of tuples.

# lst=[(),(),(","),("a","b"),("a","b","c"),("d")]
# # lst.remove((None))
# print(lst)
# lst=[tup for tup in lst if tup !=()]
# print(lst)

#WAP to unzip a list of tuples into a individual list.
# lst=[(),(","),("a","b"),("a","b","c"),("d")]
# a,b,c,d,e=lst
# print("\n",[a],"\n",[b],"\n",[c],"\n",[d],"\n",[e])

# WAP to Calculate.. the parking charges of vehicles..,
ty=['CAR',"TRUCK","SCOOTER","CYCLE","BIKE",'BUS']
c=input("\nEnter The Type Of Vehicles:")
# ho=float(input(("Enter the Number Of Hours:")))
into=float(input(("\nEnter the IN time (hh.mm):")))
out=float(input(("Enter the OUT time (hh.mm):")))


if(into and out>24):
    print("\nInvalid Input")
if(out>into):
    ho=float(out-into)
else:
    ho=float(into-out)


if (c.upper()=="BUS" or c.upper()=='TRUCK'):
    if(ho>3):
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*30)
    else:
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*20)
elif (c.upper()=='CAR'):
    if(ho>3):
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*20)
    else:
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*10)
elif(c.upper()=='SCOOTER' or c.upper()=='CYCLE' or c.upper()=='BIKE'):
    if(ho>3):
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*10)
    else:
        print("--- PARKING RECIPT ---","\n Vehicle :",c,"\n Time    :",ho,"hr","\n Charges :","Rs.",ho*5)
else:
    print("\nInvalid Input")
        
