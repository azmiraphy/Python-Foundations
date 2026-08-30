# Python Data Structures
# Topic 01 : Lists
#========================================================================


# 01 . Creating a List
#------------------------------------
subjects = [" Physics", "Mathematics", "Quantum",  "Programming","Computer Science",
            "Solid State", "Electronics","Nuclear Physics", "Atomic Physics",]
print(subjects)



# 02 . Accessing List Item
#------------------------------------
print(subjects[0])
print(subjects[2])



# 03. Negative Indexing
#------------------------------------
print(subjects[-1])
print(subjects[-2])



# 04.Changing a List item
#-------------------------------------
subjects[3]= "Scientific Computing"
print(subjects)



# 05. Listing Slicing
#-------------------------------------
print(subjects[0:2])
print(subjects[1:4])
print(subjects[2:5])
print(subjects[2:])
print(subjects[::2])



# 06. append()
# Add one item at the end
#-------------------------------------
subjects . append ("physics")
print(subjects)


# 07 .insert()
# Add item at a specific position
#-------------------------------------
subjects.insert(1,"Statistics")
print(subjects)

# 08. extend ()
# Add multiple items
#----------------------------------------
new_subjects = ["data Science ","Numerical Methods"]
subjects.extend(new_subjects)
print(subjects)


# 09. remove()
# Remove a specific item
#-----------------------------------------
subjects.remove("Computer Science")
print(subjects)

# 10.pop()
# Remove item using index
#-----------------------------------------
removed_subjects = subjects .pop(1)
print("removed:",removed_subjects)
print(subjects)

# 11. del
# delete an item
#----------------------------------------
del subjects [0]
print(subjects)


# 12. clear()
# remove all items
#------------------------------------------
numbers = [10,20,30,40]
numbers.clear()
print(numbers)

# 13.len()
# find number of items
#------------------------------------------
data = [10,20,30,40,50,60,70,80,90 ]
print("numbers of item:", len(data))


# 14. Check Item with 'in'
#-----------------------------------------
topics= [ "python","Numpy","Pandas","matplotlib"]
print("python"in topics)
print("java"in topics)


# 15. Check item with not 'in'
#---------------------------------------
print("java"not in topics )

# 16. Loop Through a List
#--------------------------------------
for topic in  topics :
    print(topic)

# 17. Numerical List
#---------------------------------------
temperatures = [ 24,25,30,35,27,29]
print (temperatures)


# 18. Sum()
#--------------------------------------
total = sum(temperatures)
print("total",total)

# 19. max() and min()
#-------------------------------------
highest = max(temperatures)
lowest = min (temperatures)
print("highest",highest)
print("lowest",lowest)

# 20. sort()
# Ascending order
#-----------------------------------------
temperatures .sort ()
print("Ascending",temperatures)

# 21 .sort(reverse = true )
# Descending order
print("Descending", temperatures)

# 22. sorted()
#-------------------------------------------
values = [ 50,20,80,10,40]
sorted_values = sorted(values)
print("Original values:",values)
print("Sorted ",sorted_values)

# 23. reverse()
#----------------------------------------
values.reverse()
print("reversed:",values)

# 24. count()
# count how many times a value appears
#----------------------------------------
numbers = [10,20,10,30,20,40]
print(numbers.count(10))

# 25. index()
# find the position of an item
#-----------------------------------------
subjects = ["physics","Math","python", "English"]
position = subjects.index("python")
print("python position:",position)

# 26. List Concatenation
#-----------------------------------------------
solar = [ 100,120,150]
wind = [ 80,110,130]
energy = solar + wind
print(energy)

# 27 . List Repetition
#------------------------------------------
numbers = [ 1,2,3]
repeated = numbers * 2
print(repeated)

# 28. Copy a List
#----------------------------------------
original = [ 10,20,30]
copied = original.copy()
copied.append(40)
print("Original:",original)
print("Copied:",copied)

# 29.  Reference vs Copy
#---------------------------------------
list_a = [1,2,3]
list_b =list_a
list_b.append(4)
print("list A:",list_a)
print("list B:",list_b)

# 30. Nested List
#---------------------------------------
student_marks = [
    [80,85,90],
    [75,88,92],
    [90,95,89]
]
print(student_marks)

#32. loop Through Nested List
#-----------------------------------------
for student  in student_marks :
    print(student)


# 31. list Comprehension
#----------------------------------------
numbers= [1,2,3,4,5,6]
squares = [number ** 2 for number in numbers]
print(squares)

# 32. list comprehension with condition
#----------------------------------------
numbers = [ 1,2,3,4,5,6,7,8,9]
even_numbers = [number for number in
numbers if number % 2 == 0 ]
print (even_numbers)


# 33. Convert Celsius to Fahrenheit
#----------------------------------------
celsius = [ 0,10,20,30,40]
fahrenheit = [
    (temperature * 9/5)+ 32
    for temperature in celsius
]

print("Celsius:",celsius)
print("Fahrenheit:", fahrenheit)

print ("               Completed             ")
