# Logical operators are used to combine conditional statements.

"""

    Operator	Description	                                                   Example	
    and 	    Returns True if both statements are true	                x < 5 and  x < 10	
    or	        Returns True if one of the statements is true	            x < 5 or x < 4	
    not	        Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)	

"""

# AND - if any one of the condition is FALSE then the result is also FALSE. 
3 > 1 and 1 in [3, 6, 8] and 3 > 4
3 > 1 and 3 in [3, 6, 8] and 4 > 3

# OR - if any one of the condition is TRUE then the result is also TRUE.
3 > 6 or 1 in [3, 6, 8] or 3 > 4
3 > 1 or 1 in [3, 6, 8] or 4 > 3

# NOT - if not TRUE --> FALSE, if not FALSE --> TRUE
3 > 4
4 > 3

# if 4 conditions then you use 4-1 and/or logic operators.
## all == and
3 > 1 and 3 in [3, 6, 8] and 3 > 2 and 7 < 9
## any == or
3 > 1 and 3 in [3, 6, 8] and 3 > 2 and 7 > 9


