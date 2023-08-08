# if is a simple conditionc statement.
# used to control the execution of set of lines or block of code or one line.

import os
terminal_width =  os.get_terminal_size().columns

the_Given_string = input("Enter the text : ")
print(the_Given_string)
user_confirmation = input("Do you want to align the text : Say YES or NO")

if user_confirmation=="yes":
    print(the_Given_string.center(terminal_width).title())
    print(the_Given_string.ljust(terminal_width).title())
    print(the_Given_string.rjust(terminal_width).title())
