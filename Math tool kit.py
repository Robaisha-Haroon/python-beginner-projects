# importing file
import utility
# Enter value and operation
number= int(input("enter a number"))
perform= int(input("""which program you want to do?
               1. Factorial
               2. Square root
               3. Prime number checker"""))
# Conditional statement
if perform == 1:
# storing function in a variable
    c= utility.factorial(number)
# printing the answer
    print("The Factorial of", number, "is", c)
elif perform == 2:
# storing function in a variable
    d= utility.sqaureroot(number)
# printing the answer
    print("The square root of", number, "is", d)
elif perform == 3:
# storing function in a variable
    e= utility.prime_check(number)
# printing the answer
    print(e)
else:
    print("Not define") 
