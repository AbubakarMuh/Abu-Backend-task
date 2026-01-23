"""
Create a custom module named calculator.py with the following functions:

1. add(a,b) to return the sum of two numbers
2. subtract(a,b) to return the difference of two numbers
3. multiply(a,b) to return the product of two numbers
4. divide(a,b) to return the division result (handle division by zero)
Then, create a separate script names main.py to:
1. import your calculator module
2. perform addition, subtraction, multiplication and division using the functions in the module

"""

'''
Then, create a separate script names main.py to:
1. import your calculator module
2. perform addition, subtraction, multiplication and division using the functions in the module

'''

from calculator import calculate_sum, calculate_sub, calculate_multiplication, calculate_divide

print("\n========================================================")
print("\n")
print(f" The out result for addition is: ", calculate_sum(2,3))
print(f" The out result for subtraction is: ", calculate_sub(1,8))
print(f" The out result for multiplication is: ",calculate_multiplication(4,10))
print(f" The out result for division is: ",calculate_divide(2,0))

# to run my code >> python3 Module_Packages/main.py