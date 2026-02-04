# Data Types in Python
# This program demonstrates different built-in data types in Python

# Numeric Types
integer_num = 10          # int: stores whole numbers
float_num = 10.5          # float: stores decimal numbers
complex_num = 3 + 5j      # complex: stores complex numbers

# Text Type
text = "Hello, Python"    # str: stores text

# Boolean Type
is_active = True          # bool: stores True or False

# Sequence Types
numbers_list = [1, 2, 3]  # list: ordered, mutable collection
numbers_tuple = (4, 5, 6) # tuple: ordered, immutable collection
number_range = range(5)  # range: sequence of numbers

# Mapping Type
student = {
    "name": "Gauri",
    "year": 3,
    "branch": "CSE"
}                          # dict: key-value pairs

# Set Types
unique_numbers = {1, 2, 3, 3}   # set: unordered, unique elements
frozen_set = frozenset([1, 2]) # frozenset: immutable set

# Display values and their data types
print("integer_num:", integer_num, "->", type(integer_num))
print("float_num:", float_num, "->", type(float_num))
print("complex_num:", complex_num, "->", type(complex_num))
print("text:", text, "->", type(text))
print("is_active:", is_active, "->", type(is_active))
print("numbers_list:", numbers_list, "->", type(numbers_list))
print("numbers_tuple:", numbers_tuple, "->", type(numbers_tuple))
print("number_range:", list(number_range), "->", type(number_range))
print("student:", student, "->", type(student))
print("unique_numbers:", unique_numbers, "->", type(unique_numbers))
print("frozen_set:", frozen_set, "->", type(frozen_set))
