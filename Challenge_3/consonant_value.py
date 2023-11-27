def solve(s):
    """Returns the highest value of consonant substrings."""
    vowels = 'aeiou'
    max_value = 0
    current_value = 0
    for char in s + 'a':  # add a vowel at the end to handle the last consonant substring
        if char in vowels:
            max_value = max(max_value, current_value)
            current_value = 0
        else:
            current_value += ord(char) - ord('a') + 1
    return max_value

print(solve("zodiacs")) 
print(solve("strength"))  

# Path: Challenge_3/consonant_value.py