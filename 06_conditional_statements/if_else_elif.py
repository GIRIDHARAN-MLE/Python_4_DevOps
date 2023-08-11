# if else statements

user_string = input("Enter the string : ")
user_confirmation = input("DO you want convert the text to title format ? say yes or no :")

if user_confirmation == "yes" :
    print(user_string.title())
else:
    print(user_string)

# if else and elif statements

a = eval(input("enter your first number : "))
b = eval(input("enter your second number : "))

if a > b :
    print(f"{a} is greater than {b}")
elif a < b :
    print(f"{a} is lesser than {b}")
else:
    print(f"{a} is equal to {b}") 
