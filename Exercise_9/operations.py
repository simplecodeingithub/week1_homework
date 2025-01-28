# Part-2: Practice with methods and functions
# Ask the user to input a value and store it in the variable 'var'
var = input("Please enter a value: ")
# print the value of 'var' in upper case using the .upper() method
print("The value of var in upper case:", var.upper())
# calculate the number of characters in 'var' without using a method
# Initialize a variable char_count to 0, to count the number of characters in var
char_count = 0
# This is a for loop that will iterate through each character in the string var.
for char in var:
    # Increments the char_count by 1 for each character in the string.
    char_count += 1
# Print the total number of characters in 'var'
print("The number of characters in var:", char_count)
# Use the isdecimal() method to check if 'var' contains only numeric characters (digits 0–9)
print("Does var contain numeric characters?:", var.isdecimal())