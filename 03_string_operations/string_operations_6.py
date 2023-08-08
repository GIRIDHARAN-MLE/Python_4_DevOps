# COUNT STRING OPERATION

the_string = "python scripting for devops"

print(the_string.count('i'))
print(the_string.count('o'))
print(the_string.count('p'))
print(the_string.count('for'))

# INDEX STRING OPERATION

print(the_string.index('p'))
print(the_string.index('p', 1))
print(the_string.index('p', 13))
print(the_string.index('p', 25))

# FIND STRING OPERATION

""" The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. 
"""
print(the_string.find('p'))
print(the_string.find('p', 1))
print(the_string.index('p', 25))
print(the_string.find('z'))
