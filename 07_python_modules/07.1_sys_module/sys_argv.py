# sys.argv returns a list of commmand line arguments passed to a script.
"""
import sys
print(sys.argv)
print(sys.argv[0]) """

# user_text = input("Enter the text : ")
# usr_action = input("Enter your action on the text (Valid Actions are upper/lower/title) : ")

import sys

if len(sys.argv) != 3 :
    print(f"{sys.argv[0]} <Please Mention your action> 'upper/lower/title'.")
    sys.exit()
user_text = sys.argv[1]
usr_action = sys.argv[2]

if usr_action == "upper" :
    print(user_text.upper())
elif usr_action == "lower" :
    print(user_text.lower())
elif usr_action == "title" :
    print(user_text.title())
else :
    print("Your action is invalid, please select the valid option.")

