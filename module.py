"""
Module: Function Challenge Set 2

Directions:
Complete each function according to its description.
Do NOT change the function names or parameters.
Each function must RETURN a value (do not print).
Your solutions must pass the automated test runner.
"""


# -------------------------------------------------
# is_even
# -------------------------------------------------
# Description:
#   Takes an integer and returns True if the number
#   is even. Returns False if the number is odd.
#
# Examples:
#   is_even(2) -> True
#   is_even(3) -> False
#   is_even(0) -> True
#
# Requirements:
#   - Must return a Boolean value (True or False).
#   - Do NOT print anything.
#
def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

    


# -------------------------------------------------
# count_vowels
# -------------------------------------------------
# Description:
#   Takes a string and returns the number of vowels
#   in the string.
#
# Vowels:
#   a, e, i, o, u (both lowercase and uppercase)
#
# Examples:
#   count_vowels("hello") -> 2
#   count_vowels("AEIOU") -> 5
#   count_vowels("xyz") -> 0
#
# Requirements:
#   - Must use iteration (a loop).
#   - Must return an integer.
#   - Do NOT print anything.
#
def count_vowels(s: str) -> int:
    vowels = ["a","e","i","o","u"]
    output = 0 

    for char in s:
        if char.lower() in vowels:
            output += 1
    return output



# -------------------------------------------------
# reverse_string
# -------------------------------------------------
# Description:
#   Takes a string and returns a new string
#   with the characters reversed.
#
# Examples:
#   reverse_string("cat") -> "tac"
#   reverse_string("") -> ""
#
# Requirements:
#   - Must return a new string.
#   - Do NOT print anything.
#   - Do NOT use built-in reverse() method.
#
def reverse_string(s: str) -> str:
    output = ""
    index = len(s)-1

    while index >= 0:
        char = s[index]
        output = output + char
        index = index - 1
    return output
    


# -------------------------------------------------
# max_of_three
# -------------------------------------------------
# Description:
#   Takes three numbers and returns the largest one.
#
# Examples:
#   max_of_three(1, 2, 3) -> 3
#   max_of_three(10, 5, 8) -> 10
#   max_of_three(-1, -5, -3) -> -1
#
# Requirements:
#   - Must use conditionals (if/elif/else).
#   - Do NOT use Python's built-in max() function.
#   - Must return the largest value.
#
def max_of_three(a: int, b: int, c: int) -> int:
    maximum = 0 
    if int > [int]-1:
        maximum += int
        return maximum
    


