# Some tips on print function

x = 2
y = 4

# This print doesn't have separator in it
print ("The multiplication of x and y is:",x*y)

# This one is gonna use separator for separating the string and multiplication!
print ("The multiplication of x and y is", x * y, sep =' :: ')

# For more info on separators check https://www.geeksforgeeks.org/python-sep-parameter-print/

# Python’s print() function comes with another parameter called ‘end‘.
# By default, the value of this parameter is ‘\n’, i.e. the new line character.

print ("satarmir")
print ("gmail.com")

# Now let's do it with 'end' parameter

print("satarmir" , end= '@')
print("gmail.com")

# For more info check https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/