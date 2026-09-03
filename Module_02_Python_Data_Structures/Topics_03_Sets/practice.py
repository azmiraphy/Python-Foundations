# Module 02 -Python Data Structures
# Topic 03 : sets
#-----------------------------------

# 1. Create a Set
numbers = {10,20,30,40,50}
print(numbers)

# 2.Remove duplicate values
data = [10,20,10,30,20,40,10]
unique_data = set(data)
print(unique_data)

# 3. Add multiple elements
numbers . update({70,80,90})
print(numbers)

# 4. Add an elements
numbers . add(60)
print(numbers)

# 5.Remove an element
numbers . remove(20)
print(numbers)

# 6. Check whether an element exists
print(30 in numbers)
print(100 in numbers)

# 7. Find the number of unique elements
print(len(numbers))

# 8 . Loop through a set
colors = {"red","green","blue"}
for color in colors:
    print(color)

# 9. Union
A = {1,2,3,4,}
B = {3,4,5,6}
print(A.union (B))
print(A|B)

# 10. Intersection
print ( A. difference (B))
print(A&B)

# 11. Difference
print(A.difference(B))
print(A-B)

# 12. Symmetric Difference
print (A.symmetric_difference(B))
print(A^B)

# 13.Remove safely using discard()
values = { 10,20,30}
values.discard(20)
values.discard(100)
print(values)

# 14 . Compare two experiment datasets
experiment_A = {10,20,30,40}
experiment_B = {30,40,50,60,}
common_values = experiment_A& experiment_B
all_values = experiment_A|experiment_B
only_A = experiment_A - experiment_B
print("Common :",common_values)
print("All Unique values :", all_values)
print("only in A:", only_A)