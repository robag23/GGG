# Create a list called menu
menu = ['Coffee', 'Tea', 'Sandwich', 'Cake']

# Create a dictionary called stock with stock values for each menu item
stock = {'Coffee': 100, 'Tea': 50, 'Sandwich': 30, 'Cake': 20}

# Create a dictionary called price with prices in pounds (£) for each menu item
price = {'Coffee': 2.50, 'Tea': 1.50, 'Sandwich': 5.00, 'Cake': 3.50}


# Calculate the total stock worth in the cafe
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print the result in pounds
print(f"The total stock worth in the cafe is: £{total_stock_worth:.2f}")