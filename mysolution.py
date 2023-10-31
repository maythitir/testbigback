# 1.
def mysolution(s):

    char_count = {}  # Dictionary to store the count of each character

    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first unique character
    for char in s:
        if char_count[char] == 1:
            return char

    # If no unique character is found, return '_'
    return '_'


# Example usage:
result1 = mysolution("abacabadabacabadeef")
result2 = mysolution("programming")
print("Example 1:", result1)
print("Example 2:", result2)
