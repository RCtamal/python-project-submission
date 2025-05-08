def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


""" # call to the factorial function
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}") """

# Get user input
try:
    number = int(input("Enter a number to calculate its factorial: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}")
except ValueError:
    print("Please enter a valid number.")

# project thoroughly and check all the validations and error handling prior to ensure it works
