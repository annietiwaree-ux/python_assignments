# ==========================================
# DICTIONARY OPERATIONS
# ==========================================

print("----- DICTIONARY OPERATIONS -----")

# 1. Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
print("Original dictionary:", student)

# 2. Access values
print("Name:", student["name"])
print("Age:", student.get("age"))

# 3. Add a new key-value pair
student["city"] = "Pune"
print("After adding city:", student)

# 4. Update an existing value
student["age"] = 21
print("After updating age:", student)

# 5. Add multiple key-value pairs
student.update({
    "college": "ABC College",
    "year": 2
})
print("After adding multiple values:", student)

# 6. Remove an item using pop()
removed_value = student.pop("city")
print("Removed city:", removed_value)
print("After pop():", student)

# 7. Remove the last inserted item using popitem()
student.popitem()
print("After popitem():", student)

# 8. Delete a specific key using del
del student["age"]
print("After deleting age:", student)

# 9. Check if a key exists
if "name" in student:
    print("Name key exists")

# 10. Get all keys
print("Keys:", student.keys())

# 11. Get all values
print("Values:", student.values())

# 12. Get key-value pairs
print("Items:", student.items())

# 13. Clear the dictionary
student.clear()
print("After clear():", student)


# ==========================================
# TUPLE OPERATIONS
# ==========================================

print("\n----- TUPLE OPERATIONS -----")

# 1. Create a tuple
numbers = (10, 20, 30, 40, 50)
print("Original tuple:", numbers)

# 2. Access elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3. Slicing
print("First three elements:", numbers[0:3])

# 4. Count occurrences
numbers2 = (10, 20, 20, 30, 20)
print("Count of 20:", numbers2.count(20))

# 5. Find index of an element
print("Index of 30:", numbers.index(30))

# 6. Check if an element exists
if 40 in numbers:
    print("40 exists in tuple")

# 7. Length of tuple
print("Length:", len(numbers))

# 8. Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print("Combined tuple:", combined)

# 9. Repeat a tuple
repeated = tuple1 * 2
print("Repeated tuple:", repeated)

# 10. Convert list to tuple
my_list = [100, 200, 300]
my_tuple = tuple(my_list)
print("List converted to tuple:", my_tuple)

# 11. Convert tuple to list
my_tuple = (100, 200, 300)
my_list = list(my_tuple)
print("Tuple converted to list:", my_list)

# 12. "Append" to a tuple
# Tuples are immutable, so we cannot directly append.
my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4,)
print("Tuple after adding 4:", my_tuple)

# 13. "Remove" an item from a tuple
# Convert tuple to list, remove the item, then convert back.
my_tuple = (1, 2, 3, 4, 5)

temp_list = list(my_tuple)
temp_list.remove(3)
my_tuple = tuple(temp_list)

print("Tuple after removing 3:", my_tuple)

# 14. Delete the entire tuple
del my_tuple

print("Tuple deleted successfully")
