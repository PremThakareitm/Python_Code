def fact(num):

    if(num < 0):
        return "We don't perform for negative values"
    
    if(num<2):
        return 1
    
    else:
        factorial = num * fact(num-1)
        return factorial

n = 1.2

while(not(int(n) == n)):
    try:
        n = int(input("Enter the num : "))
    except:
        print("We take input as integer only")

    



print(fact(n))