# THINKING EXERCISES - Day 1
# Solve each problem step by step
# Think before you code!

# ===== PROBLEM 1: Reverse a String =====
# Task: Take a sentence and print it backwards
# Example: "Hello" should print "olleH"
# Steps to think about:
#   1. What does the string look like?
#   2. How do I access each character from the end?
#   3. How do I build a new string in reverse order?

print("=== PROBLEM 1: Reverse a String ===")
sentence = "Hello Python"
# Write your code below:


# ===== PROBLEM 2: Count Vowels =====
# Task: Count how many vowels are in a string
# Vowels are: a, e, i, o, u (ignore uppercase for now)
# Example: "Hello" has 2 vowels (e, o)
# Steps to think about:
#   1. What are vowels?
#   2. How do I check each character in the string?
#   3. How do I keep track of the count?

print("\n=== PROBLEM 2: Count Vowels ===")
text = "Python is fun"
# Write your code below:


# ===== PROBLEM 3: Find Longest Word =====
# Task: Find the longest word in a sentence
# Example: "I love Python programming" -> "programming" (11 characters)
# Steps to think about:
#   1. How do I split the sentence into words?
#   2. How do I find the length of each word?
#   3. How do I compare to find the longest?

print("\n=== PROBLEM 3: Find Longest Word ===")
sentence = "I love Python programming"
# Write your code below:


# ===== PROBLEM 4: Create Initials =====
# Task: Create initials from a full name
# Example: "John David Smith" -> "JDS"
# Steps to think about:
#   1. How do I split the name into parts?
#   2. How do I get the first letter of each part?
#   3. How do I combine them into one string?

print("\n=== PROBLEM 4: Create Initials ===")
full_name = "Sandeep Kumar Singh"
# Write your code below:


# ===== PROBLEM 5: Remove Extra Spaces =====
# Task: Remove extra spaces from a string
# Example: "Hello    World" -> "Hello World"
# Steps to think about:
#   1. What causes extra spaces?
#   2. How can I replace multiple spaces with one?
#   3. Are there built-in methods that can help?

print("\n=== PROBLEM 5: Remove Extra Spaces ===")
messy_text = "Hello    World    Python"
# Write your code below:


# ===== BONUS CHALLENGE =====
# Task: Create a palindrome checker
# A palindrome reads the same forwards and backwards
# Example: "racecar" is a palindrome, "hello" is not
# Steps to think about:
#   1. How do I reverse a string?
#   2. How do I compare the original with the reversed?
#   3. How do I make it case-insensitive?

print("\n=== BONUS: Palindrome Checker ===")
word = "racecar"
# Write your code below:


# HINTS (Don't peek unless you're stuck!):
# Problem 1: Use string slicing with [::-1]
# Problem 2: Use a loop and check if character is in "aeiou"
# Problem 3: Use .split() to break into words, then find longest
# Problem 4: Use .split(), then access first letter [0] of each word
# Problem 5: Use .replace() or .split() and .join()
# Bonus: Compare word with word[::-1]
