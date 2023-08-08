#Strings
'''Strings are sequence of characters.In python, strings are surrounded by either single quotation marks, or double quotation marks.'''

'''
source_text = "hello world !!! "
java_service = "White Label Error..!!.."
multi_lines = """You can assign a multiline string to
a variable by using three quotes"""

print(f"the source value is : {source_text}\njava service text is : {java_service}\nAssign multi lines \
can be written as {multi_lines}")

'''

"""
val_empty = ""
space_value = " "   #Space is a character in python.
"""
"""
devops_scripting = "python scripting"
print(devops_scripting[0])
print(devops_scripting[5])
print(devops_scripting[0:6])
print(devops_scripting[0:-1])
print(devops_scripting[0:])
"""
#del devops_scripting
devops_scripting = "python_4_devops"
print(devops_scripting)

""" strings are immutable, we cannot modify or change strings (substring) once
assigned. But can be redefined or deleted.
"""

str_length = len(devops_scripting)
print(f"the length of the strings is : {str_length}")

print(devops_scripting[-5:-8])
print(devops_scripting[-2:-7])
print(devops_scripting[3:6])

str_1 = "python"
str_2 = "scripting"
str_3 = str_1 + " " + str_2 + " " + "for devops."
print(str_3)
