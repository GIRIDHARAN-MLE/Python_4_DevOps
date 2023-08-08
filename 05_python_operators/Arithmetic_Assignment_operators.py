# Arithmetic operators are used with numeric values to perform common mathematical operations:

"""
Operator	Name	            Example	    Result

    +	    Addition	        x + y	    it gives addition values of two operands.
    -	    Subtraction     	x - y	    it gives subraction values of two operands.
    *	    Multiplication	    x * y	    it gives multiplication values of two operands.
    /	    Division	        x / y	    it gives division values of two operands.
    %	    Modulus	            x % y	    it gives the 'remainder' value.
    **	    Exponentiation	    x ** y	    it gives the 'exponential' value.
    //	    Floor division	    x // y      it gives the 'quotient' value.

"""

# Assignment operators are used to assign values to variables:

"""
Operator	Example	    Same As	
    =	    x = 5	    x = 5	
    +=	    x += 3	    x = x + 3	
    -=	    x -= 3	    x = x - 3	
    *=	    x *= 3	    x = x * 3	
    /=      x /= 3	    x = x / 3

"""

a = eval(input("Enter the first number: "))
b = eval(input("Enter the second number: "))
result = a + b
print(f"The addition of {a} and {b} is {result} ")
