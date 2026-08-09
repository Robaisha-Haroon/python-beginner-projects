# Enter values
C_to_F= float(input("Enter Celsius value to find its Fahrenheit value\n"))
F_to_C= float(input("Enter Fahrenheit value to find its Celsius value\n"))

# Performing Tasks in variable
F_answer= (1.8*C_to_F)+32       # formule of celsius to fahrenheit ' 1.8*celcius + 32'
C_answer= (F_to_C-32)/1.8       # formule of fahrenheit to celsius ' fahrenheit-32 / 1.8 '

# Printing the result
print(f"The answer of {C_to_F} value in Fahrenheit is {F_answer}")
print(f"The answer of {F_to_C} value in Celsius is {C_answer}")
