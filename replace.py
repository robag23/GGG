# Save the sentence as a single string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Replace every "!" with a blank space
replace = sentence.replace("!", " ")

# Print the modified sentence
print("Modified sentence:", replace)

# Convert to uppercase
upper = replace.upper()

# Print the uppercase sentence
print("Uppercase sentence:", upper)

# Print the sentence in reverse
reversed = replace[::-1]
print("Reversed sentence:", reversed)