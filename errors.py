# ================== Compilation or syntax errors ==================
# These errors occur when the code violates the rules of the programming language syntax. They are usually detected by the interpreter or compiler during the code execution.

# === Example 1 ===

Print("Hello World!")

# The print keyword has a capital 'P', but  Python is case sensitive so Print and print are two different things.

# === Example 2 ===

 if x == 5;
     print("x is equal to 5")

# The semicolon is incorrectly used to indicate the end of a line of code.
# To fix this error, the semicolon should be removed and replaced with a colon ':' to indicate the start of the block of code to be executed if the condition is true.

# === Example 3 ===

moms_age = 45
   dads_age = "43"
age_difference = moms_age - dads_age
print "The age difference between mom and dad is age_difference"

# As you can see, there are a few errors in this example.
# The line 'dads_age = "43"' is unnecessarily indented.
# The variable 'dads_age' is assigned a string value instead of an integer value. This can be fixed by simply removing the quotes.
# (Alternatively, you can cast the string 'dads_age' to an integer like this 'int(dads_age)'. This is considered a runtime error (more on this below) as 'age_difference' is unable to concatenate a string and an integer type.)
# The print statement is missing parentheses and the variable 'age_difference' is missing curly braces required for f-string formatting.