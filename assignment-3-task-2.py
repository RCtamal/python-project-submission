import math

# Ask the user for a number as input
number = float(input("Enter a number: "))

# Calculate the square root of the number
square_root = math.sqrt(number)

# Calculate the natural logarithm (log base e) of the number
# Ensure the number is positive for logarithm calculation
if number > 0:
    natural_log = math.log(number)
else:
    natural_log = "undefined (logarithm of non-positive numbers is not defined)"

# Calculate the sine of the number (in radians)
sine_value = math.sin(number)

# Display the calculated results
print(f"Square root of {number}: {square_root}")
print(f"Natural logarithm of {number}: {natural_log}")
print(f"Sine of {number} (in radians): {sine_value}")
# This code calculates the square root, natural logarithm, and sine of a user-provided number.
