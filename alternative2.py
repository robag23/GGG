def alternate_case_characters(input_string):
    """
    Alternates the case of characters in the input string at the character level.

    Parameters:
    input_string (str): The input string to be processed.

    Returns:
    str: The result string with alternated case characters.
    """
    result = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_string):
    """
    Alternates the case of words in the input string at the word level.

    Parameters:
    input_string (str): The input string to be processed.

    Returns:
    str: The result string with alternated case words.
    """
    words = input_string.split()
    result = []
    for index, word in enumerate(words):
        if index % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

# Get user input with validation for empty input
user_input = input("Enter a string: ").strip()
while not user_input:
    print("Please provide a non-empty input.")
    user_input = input("Enter a string: ").strip()

# Example usage for character-level alternation using user input
output_str1 = alternate_case_characters(user_input)
print(f"Character-level alternation: {output_str1}")

# Example usage for word-level alternation using user input
output_str2 = alternate_case_words(user_input)
print(f"Word-level alternation: {output_str2}")
