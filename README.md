README for Python Challenges
This repository contains a series of Python challenges designed to test and enhance your coding skills. Each challenge focuses on different aspects of Python programming, from string manipulation to conditional logic.

Challenges Overview
Consonant Value Calculator (solve.py)
Two Positive Numbers Checker (positive_numbers.py)
12-hour to 24-hour Time Converter (time.py)
1. Consonant Value Calculator (solve.py)
This program calculates the highest value of consonant substrings in a given string. Vowels (a, e, i, o, u) are not considered, and each consonant's value corresponds to its position in the alphabet (e.g., b = 2, c = 3).

Usage Example:

python
Copy code
print(solve("zodiacs"))  # Output: 26
print(solve("strength")) # Output: 57
2. Two Positive Numbers Checker (positive_numbers.py)
This function determines whether exactly two out of three given integers are positive.

Usage Example:

python
Copy code
print(two_positive_numbers(8, 4, -3))  # Output: True
print(two_positive_numbers(-4, 3, 8))  # Output: True
print(two_positive_numbers(9, -6, 9))  # Output: False
print(two_positive_numbers(-4, 2, 0))  # Output: False
3. 12-hour to 24-hour Time Converter (time.py)
This script converts time from a 12-hour format to a 24-hour format. The input is an hour (1-12), a minute (0-59), and a period (am or pm), and it returns the time in a 24-hour format.

Usage Example:

python
Copy code
print(convert_to_24_hour(12, 30, 'pm'))  # Output: 1230
print(convert_to_24_hour(12, 0, 'am'))   # Output: 0000
Installation
Clone this repository and run each script using Python 3. Make sure Python 3 is installed on your machine.

bash
Copy code
git clone <repository-url>
cd <repository-directory>
python <script-name>.py
Contributing
Feel free to fork this repository and contribute by adding more interesting challenges or improving the existing ones. Your contributions are always welcome!