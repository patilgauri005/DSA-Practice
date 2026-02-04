'''Approach:
The idea is to take an integer input from the user and print it on the screen. This task can be broken down into the following steps:

Receive Input: Capture the integer input from the user.
Print the Input: Output the captured integer to the screen.

Use an input function to get the user's input. Return the input integer as per requirement.'''

# Function to take an integer input from the user and print it
def input_integer():
    # Step 1: Receive Input
    user_input = int(input("Enter an integer: "))
    
    # Step 2: Print the Input
    print("You entered:", user_input)

# Call the function to execute the program
input_integer()

'''Complexity Analysis:
Time Complexity: O(1) - The operations of taking input and printing output are constant time operations.
Space Complexity: O(1) - No additional space is used that grows with input size.'''