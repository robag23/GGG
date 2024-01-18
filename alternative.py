def alternate_case_characters(input_string):
    result = ""
    for index, char in enumerate(input_string):
        if index % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

def alternate_case_words(input_string):
    words = input_string.split()
    result = []
    for index, word in enumerate(words):
        if index % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

# Example usage for character-level alternation
input_str1 = 'HyperionDev'
output_str1 = alternate_case_characters(input_str1)
print(f"Character-level alternation: {output_str1}")

# Example usage for word-level alternation
input_str2 = 'Data Science bootcamp'
output_str2 = alternate_case_words(input_str2)
print(f"Word-level alternation: {output_str2}")