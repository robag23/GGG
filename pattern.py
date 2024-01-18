# Number of rows in the pattern
rows = 5

# Loop to print the pattern
for i in range(1, 2 * rows):
    # Calculate the number of stars in each row
    num_stars = i if i <= rows else 2 * rows - i

    # Print the stars for the current row
    print('*' * num_stars)