"""
Topic: Switch Case Statements (match-case)
Language: Python 3.10+
"""

# Example 1: Day of the Week
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")


# Example 2: Constant Expression
x = 10
y = 5

match x + y:
    case 15:
        print("Result is 15")
    case 20:
        print("Result is 20")
    case _:
        print("No match found")


# Example 3: Character Matching
grade = 'B'

match grade:
    case 'A':
        print("Excellent")
    case 'B':
        print("Good")
    case 'C':
        print("Average")
    case _:
        print("Not specified")


# Time Complexity: O(1) for each case, as it directly matches the value without needing to evaluate multiple conditions like in if-else statements.
# Space Complexity: O(1) for the match-case structure itself, as it does not require additional space for storing conditions or variables.