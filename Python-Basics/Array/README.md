# Arrays and Strings (DSA – Python)

This README explains **Arrays and Strings** from a **Data Structures and Algorithms (DSA)** perspective.  
The content is useful for **college exams, placement interviews, and future DSA learning**.

---

## What is an Array?

An array is a **linear data structure** used to store elements and perform operations on them.  
It allows **random access** of elements using **index values**.

An array is a collection of **similar types of elements (homogeneous elements)** stored in **contiguous memory locations**, meaning one after another in memory.

Because the elements are stored in adjacent memory blocks, accessing any element becomes very fast since the computer already knows the exact memory location of each index.

---

## Visualization of Arrays

You can visualize computer memory as a continuous block or grid where:
- Each block stores a value
- Each value has an **index**
- The first element starts at index **0**

---

## Why are Arrays 0 Indexed?

Arrays start indexing from **0** because it simplifies **memory computation**.

For an array of length `n`, valid indices are:


When an array is created, **memory is instantly reserved**.

---

## Finding an Element in an Array

There are three ways to find an element:

1. **Using Index**
   - If the index is known, the element can be accessed directly

2. **Searching Algorithms**
   - Linear Search
   - Binary Search (only for sorted arrays)

3. **Hash-Based Structures**
   - Used when faster repeated lookups are required

---

## Array Operations and Complexity

| Operation | Time Complexity |
|--------|----------------|
| Access element by index | O(1) |
| Insertion at end | O(1) |
| Insertion at beginning/middle | O(n) |
| Deletion | O(n) |
| Searching (Linear) | O(n) |

**Space Complexity:**  
- O(n), where `n` is the number of elements in the array

---

## Summary of Arrays

- Memory is allocated instantly when the array is created
- Elements are stored contiguously
- Accessing elements using index is very fast
- Arrays store homogeneous elements only
- Size and data type are defined at creation
- Insertion at end is efficient
- Insertion or deletion in middle is complex

---

## What are Strings?

Strings are a **sequence of characters** stored in a specific order.  
Each character in a string is assigned an **index starting from 0**.


---

## Accessing Characters in a String

Characters in a string can be accessed using **index values**, just like arrays.


s[0] → 's'
s[1] → 't'
---

## Length of a String

The length of a string represents the **number of characters** in it.

In Python, length can be found using: 


---

## String Concatenation

Strings can be joined together to form a new string.  
In Java, this is commonly done using **StringBuilder**, while in Python simple concatenation is used.

---

## Passing, Returning, and Assigning Strings

- Strings can be assigned like primitive types
- Assigning one string to another creates a **new copy**
- When strings are passed to functions, a copy is created
- Changes made inside a function do not affect the original string

---

## String Comparison

- `==` checks whether two strings are equal
- `!=` checks whether two strings are not equal
- Individual characters can also be compared using indices

---

## Important Notes for Interviews and Exams

- Arrays and strings use **0-based indexing**
- Arrays store **homogeneous data**
- Strings are **immutable**
- Always mention **time and space complexity**
- Arrays and strings form the foundation of most DSA problems

---
