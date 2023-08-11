# One of the method 

"""
number = eval(input("Enter any number between 1-10 range: "))

if number in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] :
    if number == 1 :
        print("one")
    elif number == 2 :
        print("two")
    elif number == 3 :
        print("three")
    elif number == 4 :
        print("four")
    elif number == 5 :
        print("five")
    elif number == 6 :
        print("six")
    elif number == 7 :
        print("seven")
    elif number == 8 :
        print("eight")
    elif number == 9 :
        print("nine")
    else :
        print("ten")
else :
    print("OUT OF RANGE, PLEASE TYPE BETWEEN 1-10 RANGE : ")

"""

# Enhaced method for writing the script

number = eval(input("Enter the number of range 0-10 : "))

dict_word = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

if number in [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] :
    print(dict_word.get(number))
else :
    print("OUT OF THE  RANGE, PLEASE TYPE BETWEEN 0-10 RANGE :")
