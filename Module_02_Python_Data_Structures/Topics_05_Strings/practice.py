# Module 02
# Topic 05- Python Data Structures
#------------------------------------------

# 1. Create A string
name = "Azmira"
subject = "Physics"
print(name)
print(subject)

# 2. String Indexing
word = "Physics"
print(word[0])
print(word[1])
print(word[5])

# 3.Negative Indexing
print(word[0:3])
print(word[2:6])

# 4. String slicing
print(word[0])
print(word[0:3])
print(word[2:6])
print(word[2:])

# 5.String Length
print(len(word))

# 6. String Concatenation
first_name = "Azmira"
last_name = "Khatun"
full_name = first_name + " " + last_name
print(full_name)

# 7. String Repetition
message = "Solid State"
print(message*3)

# 8. Check weather text exists
text = " I study physics"
print("physics " in text)
print("Quantum" in text)
print(" physics" not in text)

# 9. Loop through a string
word  = "physics"
for letter in word :
    print (letter)

# 10. Change case
text = "python programming"
print(text.lower())
print (text.upper())
print(text.capitalize())
print(text.title())

# 11. Remove extra spaces
text = "       physics    "
print(text.strip())

# 12. Replace text
text = "I study physics"
new_text = text.replace("physics","math")
print(new_text)

# 13.Split String
text = "physics mathematics Quatum"
subjects = text. split()
print(subjects)

# 14. Join Strings

subjects = ["physics", "Math", "Quantum"]
text = ",".join(subjects)
print(text)

# 15. Find Text
text = "Python programming "
print(text.find("Programming"))
print(text.find("java"))

# 16. Count Characters
text = "banana"
print(text.count("a"))
print(text.count("b"))

# 17 . Check String and finding
filename = "solar_data.csv"
print(filename.startswith("solar"))
print(filename.endswith("solar"))

# 18. Check String Content
number = "123"
text = "physics"
print(number.isdigit())
print(text.isalpha())

# 19. Covert Number to string
age = 23
age_text = str(age)
print(age_text)
print(type(age_text))

# 20. f - string
name = "Azmira"
subject = "physics"

print (f"my name is {name} and I study {subject}.")

# 21.  Scientific Data Using Strings
quantity = "temperature"
value = 300
unit = "k"
print(f"{quantity} = {value}{unit}")

# 22. Physics Measurement
measurement = {
    "quantity": "length",
    "value": 10.5,
    "unit": "cm"
}

# 23. List of Scientific Labels
quantities = [
    "temperature",
    "pressure",
    "velocity",
    "Acceleration"
]
for quantity in quantities:
    print( quantity)


# 24. File Name Checking
filename = "expertiment_data.csv"
if filename.endswith(".csv"):
    print("csv file detected")

print(" --------------------- Practice  completed ---------------------------")
