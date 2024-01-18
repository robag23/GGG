# Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Calculate and display the length of str_manip
length_of_str_manip = len(str_manip)
print("Length of str_manip:", length_of_str_manip)

# Find the last letter in str_manip sentence and replace every occurrence with '@'
last_letter = str_manip[-1]
str_manip_with_at = str_manip.replace(last_letter, '@')

# Print the modified string
print("Modified str_manip with '@':", str_manip_with_at)

# Print the last 3 characters in str_manip
last_three_characters = str_manip[-3:]
print("Last 3 characters in str_manip:", last_three_characters)

# Create a five-letter word using the first three and last two characters of str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print("Five-letter word:", five_letter_word)