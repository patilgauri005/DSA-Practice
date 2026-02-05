## If-Else Statements in Python

### What are Conditional Statements?
Conditional statements allow a program to make decisions based on conditions.
They execute different blocks of code depending on whether a condition is true or false.

### The `if` Statement
The `if` statement executes a block of code only when the given condition is true.

### The `else` Statement
The `else` statement executes when the condition in the `if` statement is false.

### The `elif` Statement
`elif` (else if) is used to check multiple conditions sequentially.
Once a condition is satisfied, the remaining conditions are skipped.

---

### Example 1: Adult Check
- Takes age as input
- Checks if age is greater than or equal to 18
- Prints whether the person is an adult or not

### Example 2: Student Grading System
Grades are assigned based on marks:
- Less than 25 → Grade F
- 25–44 → Grade E
- 45–49 → Grade D
- 50–59 → Grade C
- 60–69 → Grade B
- 70 and above → Grade A

The grading logic is simplified by checking only the upper bounds using `elif`.

### Key Takeaways
- Conditional statements control program flow
- `elif` improves readability and reduces redundancy
- Proper ordering of conditions is important
