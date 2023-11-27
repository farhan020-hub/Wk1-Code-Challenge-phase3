
def two_positive_numbers(a, b, c):
    """Returns True if exactly two of the three integers are positive numbers, and False otherwise."""
    count = 0
    for num in (a, b, c):
        if num > 0:
            count += 1
    return count == 2

print(two_positive_numbers(8, 4, -3))  
print(two_positive_numbers(-4, 3, 0))  


# Path: Challenge_2/positive_numbers.py