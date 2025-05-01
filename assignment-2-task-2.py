# Initialize a variable to store the sum
total_sum = 0

# Using a for loop over numbers from 1 to 50
for number in range(1, 51):
    total_sum += number  # Adding each number to total_sum

# Displaying the final sum
# Using f-string to directly insert 'number' into the string output
print(f"The sum of numbers from 1 to 50 is: {total_sum}")