# JOIN STRING OPERATION

x = "Python"
y = "-".join(x)

print(y)

print("*".join(x))
print("\n".join(x))
print("\t".join(x))

# CENTER STRING OPERATION

the_string = "Python"
the_new_string = "Scripting for DevOps"
other_string = "STRING OPERATION"

print(f" {the_string.center(20)} \n{the_new_string.center(20)} \n{other_string.center(20)}")

# ZFILL STRING OPERATION

print(the_string)
print(the_string.zfill(10))  #The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
