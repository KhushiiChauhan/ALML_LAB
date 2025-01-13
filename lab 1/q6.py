# Create a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]

# Accessing elements using indexing
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# Modify elements in the list
fruits[1] = "Kiwies"
print(f"\nModified list after changing the second fruit: {fruits}")

# Add elements to the list
fruits.append("Watermelon")
print(f"\nList after adding 'Watermelon': {fruits}")

# Remove an element from the list
fruits.remove("Watermelon")
print(f"\nList after removing 'Watermelon': {fruits}")

# Find the length of the list
length = len(fruits)
print(f"\nThe length of the list is: {length}")

# Sort the list in ascending order
fruits.sort()
print(f"\nSorted fruits list in ascending order: {fruits}")

# Sort the list in descending order
fruits.sort(reverse=True)
print(f"Sorted fruits list in descending order: {fruits}")
