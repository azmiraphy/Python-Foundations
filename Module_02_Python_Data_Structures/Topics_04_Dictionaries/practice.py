# Module 02 - Python Data Structure
# Topic 04 - Dictionaries
#-----------------------------------------------

# 1. Create a Dictionaries
student = {
    "name": " Azmira",
    "age" : 23,
    "subject": "Physics"
}
print(student)

# 2. Access values using keys
print(student["name"])
print(student["subject"])

# 3. Add a new key-value pair
student["cgpa"] = 3.82
print(student)

# 4. Update an existing value
student["age"] = 23
print(student)

# 5. Using get()
print(student.get("name"))
print(student.get("cgpa"))

# 6.Dictionary len
print(len(student))

# 7. Get all values
print(student.values())

# 8. Get all keys
print(student.keys())

# 9. Get keys-value pairs
print(student.items())

# 10 . Loop Through Dictionary
for key , value in student.items():
    print(key,":",value)

# 11 . Remove an item using pop()
student.pop("age")
print(student)

# 12 . Add multiple items using update()
student.update({
    "age":23,
    "university":"National University"
})
print(student)

# 13 . Physics Data Using Dictionary
object_data = {
    "mass": 5,
    "velocity": 10,
    "acceleration": 2
}
print("mass:",object_data["mass"])
print("velocity:",object_data["velocity"])
print("acceleration:", object_data["acceleration"])

# 15 . Calculate kinetic energy using Dictionary Data
mass = object_data["mass"]
velocity = object_data["velocity"]
kinetic_energy = .5 * mass * velocity ** 2
print(kinetic_energy)

# 16. Scientific measurement data
measurement = {
    "quantity":"length",
    "value" : 10.5,
    "unit" : "cm"
}

# 17.List of Dictionary
experiment = [
    {"temperature":300,"pressure":10230},
    {"temperature":310,"pressure":12344},
    {"temperature":420,"pressure":34567}

]
for experiment in experiment:
    print(
        "temperature:",experiment["temperature"],
        "pressure:",experiment["pressure"]
    )


