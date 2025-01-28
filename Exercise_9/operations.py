# Part-2: Practice with methods and functions
# Ask the user to input a value and store it in the variable 'var'
var = input("Please enter a value: ")
# print the value of 'var' in upper case using the .upper() method
print("The value of var in upper case:", var.upper())
# calculate the number of characters in 'var' without using a method
# Initialize a counter to count the number of characters in var
char_count = 0
# it is a for loop,iterates through each character in the string var
for char in var:
    # Increment the counter for each character
    char_count += 1
# Print the total number of characters in 'var'
print("The number of characters in var:", char_count)
# Use the isdecimal() method to check if 'var' contains only numeric characters (digits 0–9)
print("Does var contain numeric characters?:", var.isdecimal())