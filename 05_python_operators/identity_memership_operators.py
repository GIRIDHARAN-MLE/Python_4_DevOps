# Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location. 

"""
Operator	    Description	                                            Example	
    is 	        Returns True if both variables are the same object	    x is y	
    is not	    Returns True if both variables are not the same object	x is not y

"""

# Membership operators are used to test if a sequence is presented in an object.

"""
    Operator	Description	                                                                     Example 
    in 	       Returns True if a sequence with the specified value is present in the object	      x in y	
    not in	   Returns True if a sequence with the specified value is not present in the object   x not in y

"""

valid_java_version = [ "1.6", "1.8", "1.8.6"]
host_java          = [ "1.5" ]

if host_java in valid_java_version:
    print("Host deployed of valid java version.")
else:
    print("Host deployed with invalid java version.")

db_users = [ "db_admin", "db_conf_user", "db_dev" ]

random_users = "db_admin"

if random_users in db_users :
    print(" YES, THIS USER IS ALLOWED TO START THE DB ")
else:
    print(" NO, THIS USER IS NOT ALLOWED TO START THE DB ")




