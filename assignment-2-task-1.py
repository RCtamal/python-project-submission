# The code takes an integer input from the user and checks if it is even or odd.

# It prints "Even" if the number is even and "Odd" if the number is odd.
number = (int(input("Enter a number: ")))

# Initially, one might consider using '/' to check divisibility,
# but '/' gives a decimal result, which is not ideal for checking even or odd.
# Instead, we use '%' to find the remainder when divided by 2.
if number % 2 == 0:

    # Using f-string to directly insert 'number' into the string output
    print(f"{number} is even number.")
else:
    print(f"{number} is odd number.")
print("Thank You")
# The code uses the modulo operator (%) to determine if the number is even or odd.
# If the remainder when the number is divided by 2 is 0, it is even; otherwise, it is odd.