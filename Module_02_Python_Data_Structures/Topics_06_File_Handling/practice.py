# Module 02 - Python Data Structures
# Topic 06 - File  Handling
# ------------------------------------------

# 1. Create and Write to a File
with open ("data.txt","w") as file:
    file.write("Physics\n")
    file.write("Math\n")
    file.write("Quantum\n")

# 2 . Read the Entire File
with open ("data.txt","r") as file:
    data = file.read()
print("file content:")
print(data)

# 3.Read All Lines
with open ("data.txt","r") as file:
    lines = file.readlines()
print("All lines :")
print(lines)

# 4. Read file using loop
print("subjects")
with open ("data.txt","r") as file:
    for line in file :
        print(line.strip())

# 5 . Append New Data
with open ("data. txt","a") as file:
    file.write("Computer Science\n")

# 6 . Check Update File :
with open ("data.txt","r")as file:
    print("\nupdated file :")
    print(file.read())

# 7 . Scientific Data File :
with open ("temperature . txt","w") as file:
    file.write(" 300\n ")
    file.write(" 305\n ")
    file.write("310\n ")
    file.write(" 315\n ")

# 8. Read Scientific Data:
with open ("temperature . txt","r") as file:
    data = file.readlines()

temperature = []
for value in data :
    temperature.append(str(value.strip()))
print("temperature:",temperature)

# 9. Find Maximum and Minimum :
print("Maximum temperature :",max (temperature))
print("Minium temperature :",min (temperature))

# 10. Scientific Measurement File :
with open ("measurement.txt","w") as file:
    file.write("length = 10.5 cm\n")
    file.write("temperature = 300 k\n")
    file.write("pressure = 12345 pa\n")

# 11 . File + Dictionary
with open ("object.txt","w") as file:
    file.write("mass=\n")
    file.write("velocity=10\n")
    file.write("acceleration=2\n")
data = {}

# 12. Save Calculation Result to a File:
mass = 50
velocity = 10
kinetic_energy = .5* mass* velocity** 2
with open ("result.txt","w") as file :
    file.write(f"Mass = {mass} kg\n")
    file.write(f"Velocity = {velocity}m/s\n")
    file.write(f"kinetic energy = {kinetic_energy} j\n")
    print("Result saved to result .txt")

