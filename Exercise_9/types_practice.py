# Part-1: Practice declaring variables and using different types
# created the 2 variables first_name and last_name
# Assign the first name to the variable 'first_name'
first_name = "Chaitra"
# print the value of 'first_name'
print(first_name)
# print the data type of 'first_name'
print(type(first_name))

last_name = "Boregowda"
print(last_name)
print(type(last_name))

# Concatenated 'first_name' and 'last_name' with a space in between and assign it to 'full_name'
full_name = first_name + ' ' +  last_name
# Print the value of full_name
print(full_name)
print(type(full_name))

# transfer these variable values into a list and display the list and list mutable(can change)
names_list = ['Chaitra','Boregowda']
print(names_list)
print(type(names_list))
print(names_list[0])
print(names_list[1])
# print(names_list[2])
names_list.append('CB')
print(names_list)
print(names_list[2])

# take the variables & now store the values in the dictionary using keys first and last
# dictionary is mutable
names_dictionary = {'first': 'Chaitra','last': 'Boregowda'}
print(names_dictionary)
print(type(names_dictionary))

# Adding one more key value pair to the dictionary
names_dictionary['middle'] = 'CB'
print(names_dictionary)

# # Accessing values using keys
# first_name1 = names_dictionary.get('first')
# last_name1 = names_dictionary.get('last')
# print(first_name1)
# print(last_name1)

