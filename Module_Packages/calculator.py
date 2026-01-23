import logging # Logging of errors
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


print("add(a,b) to return the sum of two numbers")
print("\n")

def calculate_sum(a,b):
    return (a + b)

def calculate_sub(c,d):
    return (c - d)

def calculate_multiplication(e, f):
    return (e * f)

# Use case1: Error handling for division by Zero
def calculate_divide(l, m):
    try:
        result = l / m
        logging.info(f"Division successful: {result}")
        return result
    except ZeroDivisionError:
        logging.warning("Attempted division by zero")
        return None
    except Exception:
        logging.exception("Unexpected error during division")
        return None

Sum_Out_Put = calculate_sum(1,2)
Subtraction_Out_Put = calculate_sub(2,3)
Multiplication_Out_Put = calculate_multiplication(2,3)
Multiplication_Out_Put = calculate_multiplication(2,3)
Division_Out_Put = calculate_divide(10,0)

# Use case2: Error handling for division by Zero
logging.basicConfig(
    filename = "app.log",
    level= logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

n = None
for i in range(10):
    for j in range(0, 1):
        if j == 0:
            logging.warning(f"Skipping division i = {i}, j = {j}")
            continue
        try:
            n = i / j
            logging.info(f"Result: n = {n}")
        except ZeroDivisionError:
            logging.exception(f" Unexpected error occur.")
            
if n is not None:
    print(f"The result for n is: {n}")
else:
    print("Division_out_put: No valid division was performed")


print(f"Out put of 2 addition numbers are: ", Sum_Out_Put)
print(f"Out put of 2 sub numbers are: ", Subtraction_Out_Put)
print(f"Out put of 2 multiplication numbers are:", Multiplication_Out_Put)
print(f"Out put of 2 division numbers are:", Division_Out_Put)


# to run my code >> python3 Module_Packages/calculator.py