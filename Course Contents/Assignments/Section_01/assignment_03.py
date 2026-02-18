# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable will contain only 4 characters

    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>

"""

chars = "[[]]"
word = "Cool"

# Expected Result Printed: [[Cool]]

# Your code below:

result = chars[:2] + word + chars[2:]
print(result)

"""
Python string slicing works like this: string[start:end]

chars[:2]
From the beginning up to (but not including) index 2"
Takes indices 0 and 1 → "[["

chars[2:]
From index 2 to the end of the string"
Takes indices 2 and 3 → "]]"

Then Python does:
"[[" + "Cool" + "]]"
"""































# Solution Below:
# print(chars[:2] + word + chars[2:])


