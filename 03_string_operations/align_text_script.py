# command to check status of display  terminal column in linux is "tput cals" manually

# command to check status of display  terminal column in windows is "mode" manually

import os
terminal_width =  os.get_terminal_size().columns

the_Given_string = input("Enter the text : ")

print(the_Given_string.center(terminal_width).title())
print(the_Given_string.ljust(terminal_width).title())
print(the_Given_string.rjust(terminal_width).title())
