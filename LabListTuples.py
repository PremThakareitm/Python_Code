#WAP to create list tuple and dictionaries of 7 elements
#WAP tuple with different datatype.
#WAP to arrange list is decending order of elements

# lst=[1,"Prem",36,12,"thakare","ITM",43]
# tpl=(1,32,"thakare.prem",23,0,"thakare.",90)
# dit={1:"thakare","ITM":36}



    
# lst =[1,34,45,64,21,12,8]
# l=len(lst)

# for i in range(l):
#     for j in range(i + 1,l):

#         if lst[i] > lst[j]:
#             lst[i],lst[j] =lst[j],lst[i]

# print(lst)

# lst =[1,34,5,64,"Prem",72,8,99]
# l=len(lst)
# max=lst[0]
# for i in range(0,l):
#     if (lst[i]>max):
#         max=lst[i]
#         print(lst[i])

#WAP to demonstrate control statement break

# for i in range(0,5):
#     if(lst[i]=="Prem"):
#         break
#     print(lst[i])
# print(lst)

# passs=input("Enter the Password:")
# while(passs="2601"):
    
    
#WAP to manage library catlog control search and checkout the book in library system.

bookss=[]
bookss=["Hc Verma", "Physics","Python Software","S.Chand","Chem"]
print(bookss)
let=len(bookss)
cho=int(input("Enter the Operation\n1.Book Search\n2.CheckOut the Book\n3.Add the Book\n:"))

if(cho==1):
    ser=input("Select the Book:")
    for i in range(0,let):
        if(bookss[i]==ser):
            print("Book Found\n")
            break
    else:
        print("Book not found\n")
elif(cho==2):
    ser=input("Select the Book to Checkout:")
    for i in range(0,let):
        if(bookss[i]==ser):
            bookss.remove(bookss[i])
    else:
        print("Book not found\n")
else:
    n = int(input("Enter the Number of Books to be added : "))
    for i in range(0,n):  
        ado=input()
        bookss.append(ado)
print(bookss)
    
    