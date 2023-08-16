#!/usr/bin/python3

""" getpass() prompts the user for a password without echoing. the getpass module provides
a secure way to handle the password prompts where programs interact with the users via the terminal.

"""

import getpass
db_pass = getpass.getpass(prompt = "Enter the DB Password: ")

print(f"The entered password is: {db_pass}")

""" getuser() function displays the login name of the user. this function checks the environment variables
LOGNAME, USER, LNAME and USERNAME, in order, and returns the value of the first non-empty string.

"""

import getpass as gp 
print(gp.getuser())
