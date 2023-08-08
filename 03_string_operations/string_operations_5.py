# STRIP STRING OPERATION

the_string = "   python        "

print(the_string)
print(the_string.strip())

print(the_string.strip('p'))
print(the_string.strip('n'))    #The strip() method returns a copy of the string in which all chars have been stripped from the beginning and the end of the string.
print(the_string.strip('t'))

the_new_string = "python scripting for devOps"
print(the_new_string.strip('devOps'))

the_new_string_1 = "python scripting for devOps python" 

print(the_new_string.strip('python'))
print(the_new_string.rstrip('python'))
print(the_new_string.lstrip('python'))

the_new_string_2 = "python./d"
the_new_string_2 = the_new_string_2.strip('./d')
print(the_new_string_2)

the_new_string_3 = "pythonyyy" # CAN ADD MULTIPLE STRIP 
print(the_new_string_3.strip('p').rstrip('y').lstrip('y').strip('y'))

# SPLIT STRING OPERATION

the_string = "python scripting for devOps"
print(the_string.split())   # The split() method splits a string into a list.
print(the_string.split('for'))

