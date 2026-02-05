# array_operations.py
# Topic: Insert, Delete, Search

arr = [10, 20, 30, 40]

# Insert element at end
arr.append(50)
print("After insertion:", arr)

# Insert at specific index
arr.insert(2, 25)
print("After inserting at index 2:", arr)

# Remove element
arr.remove(30)
print("After deletion:", arr)

# Linear search
key = 40
found = False

for i in range(len(arr)):
    if arr[i] == key:
        found = True
        print("Element found at index:", i)
        break

if not found:
    print("Element not found")
