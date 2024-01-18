# Initialize variables
total = 0
count = 0

# Continuously ask the user for input
while True:
    user_input = input("Enter a number: ")

    # Check if the user wants to stop
    if user_input == '-1':
        break

    # Try to convert the input to a number
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Update the total and count
    total += number
    count += 1

# Calculate the average (if at least one number was entered)
if count > 0:
    average = total / count
    print(f"The average of the entered numbers is: {average}")
else:
    print("No valid numbers entered.")