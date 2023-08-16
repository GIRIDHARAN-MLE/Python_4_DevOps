""" The platform module is used to access the underlying platform's data such as hardware, operating
system and interpreter version info. etc..,.. """

# platform module can be used and imported as :

#1. import platform

#2. import platform as pt

#3. from platform import *

#4. from platform import system, platform

""" to list all functions and methods in a module : dir()

print(dir(platform))

to get a help of the modules use help() :

print(help(platform))

"""

import platform as pf

print(f"This is {pf.system()} OS.")
print(f"Python Version is : {pf.python_version()}")

print(pf.python_version_tuple())
print(pf.machine())
print(pf.release())
print(pf.platform())
print(pf.architecture())
print(pf.processor())
print(pf.node())
print(pf.uname())

