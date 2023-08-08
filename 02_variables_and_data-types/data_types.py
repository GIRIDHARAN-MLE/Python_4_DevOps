# DATA TYPES IN PYTHON

'''
Every value in python has a data type, since everything is an "object" in python programming, 
data types are "classes" and variables are instance (object) of these classes.
'''

#DIFFERENT DATA TYPES IN PYTHON

'''
* Numeric data type - int, float and complex

* Text - string data type

* Boolean data type
'''

x = 5
y = 8.6
z = 7 + 5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

x = 6; y = 7.5; z = 2 + 4j
print(x, y, z)

text_content = "hello world !!"
print(text_content)

bool_value_0 = True
bool_value_1 = False

print(bool_value_0, type(bool_value_0))
print(bool_value_1, type(bool_value_1))

x = 8
print(x, type(x))
y = str(x)
print(y, type(y))
z = bool(x)
print(z, type(z))

p = 0
print(p, type(p))
q = bool(p)
print(q, type(q))

e = "8.5.36.0"
f = int(e)
print(f, type(f))

"""
NOTE : 
Any data type can be converted into boolean.
Any data type can be converted into string but reverse is not always true.
"""
