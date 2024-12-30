# Ask the user to input a number
n = int(input("Enter a non-negative integer: "))

# Check if n is 0
if n == 0:
    result = 0.0  # If n is 0, the result is 0
# Check if n is 1
elif n == 1:
    result = 1.0  # If n is 1, the result is 1
else:
    sum = 0.0  # Initialize sum to 0
    # Loop to calculate the sum for n >= 2
    for i in range(1, n + 1):  # Loop through numbers from 1 to n
        sum += (n - i + 1) / i  # Add the fraction to the sum
    result = round(sum, 2)  # Round the result to 2 decimal places

# Print the result
print("The fractional sum for n = ", n, " is: ", result)