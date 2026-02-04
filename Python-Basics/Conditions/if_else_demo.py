# If-Else Statements in Python
# This program demonstrates basic if-else and else-if (elif) conditions

# -----------------------------
# Example 1: Check if a person is an adult
# -----------------------------

age = int(input("Enter your age: "))

if age >= 18:
    # This block executes if the condition is true
    print("You are an adult.")
else:
    # This block executes if the condition is false
    print("You are not an adult.")

# -----------------------------
# Example 2: Grading system using if-elif-else
# -----------------------------

marks = int(input("Enter your marks: "))

if marks < 25:
    print("Grade: F")
elif marks <= 44:
    print("Grade: E")
elif marks <= 49:
    print("Grade: D")
elif marks <= 59:
    print("Grade: C")
elif marks <= 69:
    print("Grade: B")
elif marks >= 70:
    print("Grade: A")
else:
    print("Invalid marks entered")
