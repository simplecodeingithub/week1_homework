# hash bang - shebang
#!/usr/bin/python
# we use import to import the sys module to access the command line arguments
# making the code in the sys file (aka module) available to my anatomy.py script
# package is a collection of module
import sys
# argc is a variable assigned the length of sys.argv,argv is a part of sys
argument_count = len(sys.argv)
print(argument_count)
print("number of arguments" + ' ' + str(argument_count))

#  this is if-else statement
# If there is more than one command-line argument,it will print 'too many args'
if argument_count > 1:
    print('too many args')
    print("Please try again")
# if it is not more than one, it will print "Hello" and Assign the value 'world' to the variable 'where'
else:
    where = 'world'
    #  this is the print function doing concatenation
    #  Concatenation is gluing strings together
    #  we are passing 2 arguments
    #  "Hello" is the zeroth argument to the print function
    # the where variable the list arg to print

    print("Hello", where)
    print("zero","one","two", "three", "four")

# this will Print a goodbye message followed by the script name(which is the 1st item in the sys.argv)
#  string + string
print(' goodbye from ' + sys.argv[0])
print(' goodbye from ' + sys.argv[0], "!!!")
print('one', 'two', 'three')
# use seperator
print("zero","one","two", "three", sep="_")
print("zero","one","two", "three", sep="!!!", end="!\n\n\n")
print(' goodbye from ' + sys.argv[0])
# print(' goodbye from ' +  sys.argv[1])