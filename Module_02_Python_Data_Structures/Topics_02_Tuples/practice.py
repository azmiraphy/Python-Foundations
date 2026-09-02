# Module 02 - Python Data Structures
# Topic 02 - Tuples
#----------------------------------------

# 1. Create a tuple
numbers = ( 10,20,30,40,50)
print(numbers)

# 2. Access tuple elements using index
print(numbers[0])
print(numbers[2])
print(numbers[-1])

# 3. Tuple slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# 4 . Check if an element exists
print(30 in numbers)
print(100 in numbers )

# 5. Count an element
values = (10,20,10,30,10,40)
print(values.count(10))

# 6. Tuple length
print(len(numbers))

# 7. find the index of an element
print(values .index(30))

# 8. Loop through a tuple
colors = ("Red","Green", "Blue")
for color in colors :
    print(color)

# 9. Tuple unpacking
student = ("Azmira ",3.82 ,"Physics")
name, cgpa, subject = student
print(name)
print(cgpa)
print(subject)

# 10. Single_element Tuple
single_value = (100,)
print(single_value)
print(type(single_value))

# 11. Nested tuple
coordinates = ((10,20),(30,40),(50,60))
print(coordinates[0])
print(coordinates[1][0])

# 12. Tuple with physics data
measurement = (" Lenghth", 10.5,"cm")
quality , value,unit = measurement
print("Quality:", quality)
print("value:", value)
print("unit:",unit)

# Function returning multiple
def calculate_motion(distance,time):
    velocity = distance/time
    return distance,time,velocity
result = calculate_motion(100,5)
print(result)

# Unpacking returned tuple
distance,time,velocity = calculate_motion(100,5)
print("Distance:", distance)
print("Time:",time)
print("velocity:",velocity)

# 14. Demonstrating immutability
data = (10,20,30)

# The Following line will give an error:
# data [0]= 100
print(data)


