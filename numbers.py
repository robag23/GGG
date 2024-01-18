# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate and print the results
sum_of_numbers = num1 + num2 + num3
difference_first_second = num1 - num2
product_third_first = num3 * num1
sum_divided_by_third = (num1 + num2 + num3) / num3

# Print the results
print("Sum of all numbers:", sum_of_numbers)
print("First number minus second number:", difference_first_second)
print("Third number multiplied by first number:", product_third_first)
print("Sum of all three numbers divided by third number:", sum_divided_by_third)