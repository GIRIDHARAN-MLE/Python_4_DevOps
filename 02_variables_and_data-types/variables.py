'''Variables are the names that are used to assign for the data which stores different types of values
that reserves some specific memory location.'''

# Assign values to a Variable.
x = 4        
print(x)
print('x')
print(type(x))  # type() function tells the type of the specific objects. 

y = 5.7
print(y)
print(type(y))  

#Re-declaring the variable
x = 27
print(x)

del x
print(x)

x = 28
print(id(x))    #Python id() function returns the “identity” of the object.

#Rules to define Python variables:

'''
1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. Variable name should not be a reserved or keyword in python.
6. Variable name should not contain "spaces".

Example :

* Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

* Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"
'''
