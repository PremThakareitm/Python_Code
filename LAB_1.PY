#1 Question
#1.⁠ ⁠Write a python function to find maximum of three numbers

def find_max(num1, num2, num3):
    max_num = max(num1, max(num2, num3))
    return max_num
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Display
maximum = find_max(num1, num2, num3)
print("The maximum among {}, {}, and {} is: {}".format(num1, num2, num3, maximum))

#2 Question
#Write a python function to sum all numbers in a list
def sum_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers_list = [1, 2, 3, 4, 5]

result_sum = sum_of_numbers(numbers_list)

print("The sum of the numbers in the list {} is: {}".format(numbers_list, result_sum))

#3 Question
#Write a python function to multiply all numbers in a list
def multiply_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    
    return product
#list
numbers_list = [1, 2, 3, 4, 5]
#print 
result_product = multiply_numbers(numbers_list)
print("The product of the numbers in the list {} is: {}".format(numbers_list, result_product))

#4
#Write a python function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

string_to_reverse = input("Enter a string to reverse:")
reversed_string = reverse_string(string_to_reverse)
print(reversed_string)
#5
#Write a python function to calculate factorial of a number (non-negative integer)
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)

    print("The factorial of {} is: {}".format(num, result))
#6
#Write a python function to find square and cube of a number

def square(number):
    return number ** 2

def cube(number):
    return number ** 3

num = 5

result_square = square(num)
print(f"The square of {num} is: {result_square}")

result_cube = cube(num)
print(f"The cube of {num} is: {result_cube}")

#7
def remove_duplicates(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result_list = remove_duplicates(sample_list)
print("Original list: ",sample_list)
print("List with distinct elements: ",result_list)

#8
#Write a python function that accepts a string and counts the number of upper and lower case letters
#string_test = 'today is my best day'
def count_upper_lower(string):
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

string_test = 'today is my best day'
upper, lower = count_upper_lower(string_test)
print("Original string:",string_test)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters: ",lower)

#9
#wap to check wether a program is perfect or not



#10
#Write a python function that checks weather a passed string is a palindrome or notdef is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_string == cleaned_string[::-1]


string_to_check = "A man, a plan, a canal, Panama"
result = is_palindrome(string_to_check)

if result:
    print(string_to_check, "is a palindrome.")
else:
    print(string_to_check,"is not a palindrome.")