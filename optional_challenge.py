# Compilation Error 1: Missing closing parenthesis
print("Hello, World!"  # Syntax error: Missing closing parenthesis

# Compilation Error 2: Undefined variable
message = "This is a message"
print(mesage)  # NameError: 'mesage' is not defined, misspelling

# Runtime Error: Division by zero
numerator = 10
denominator = 0
result = numerator / denominator  # ZeroDivisionError: division by zero

# Logical Error: Incorrect calculation of the area
def calculate_area(length, width):
    # Incorrect formula for calculating area
    area = length * width  # Should be length + width
    return area

# Test the function with a rectangle
length = 5
width = 3

result = calculate_area(length, width)
print(f"The area of the rectangle is: {result}")