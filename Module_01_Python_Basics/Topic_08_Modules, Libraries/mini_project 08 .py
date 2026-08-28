# Mini Project 08 : Physics Scientific Calculator
# Topic 08 : Modules and Libraries
# Author : Azmira Khatun

import math
# Function 1 : Calculate Square Root
#============================================
def calculate_square_root(number ):
    return math.sqrt(number)



# Function 2: Calculate Circle Area
#=============================================
def calculate_circle_area(radius):
    return math.pi * radius**2


# Function 3 : Trigonometric Values
#================================================
def calculate_trigonometry(angle):
    radians = math.radians(angle)
    sine = math . sin(radians)
    cosine = math. cos (radians)
    tangent = math . tan(radians)
    return sine,cosine,tangent


# ==================================================
# Main program
#===================================================
print("========================= Physics Scientific Calculator ==================")
print("=============================================")
print()
print("1. Square root")
print("2. Circle Area")
print("3.Trigonomertic values")
print()
choice = int(input("Enter your choice(1-3):"))
print()



# Square Root
if choice == 1 :
    number = float(input("enter a positive number:"))
    if number >= 0 :
        result = calculate_square_root(number)
        print("square root =",
              round(result,4)
              )
    else:
        print("error cannot be negative")



# Circle Area:
elif choice == 2 :
    radius = float(input("enter radius (m)"))
    if radius >= 0:
        area = calculate_circle_area(radius )
        print(
              "Circle Area =",
              round(area,4),
               "m^2"
        )
    else:
        print("Error cannot be negative")



# Trigonometric Values
elif choice == 3 :
     angle = float(input("enter angle (degrees)"))
     sine,cosine,tangent = calculate_trigonometry(angle)
     print("sin(",angle,") =",
           round(sine,4,))
     print("cos(",angle,") =",
           round(cosine,4,))
     print("tan(",angle,") =",
           round(tangent,4,))



# Invalid choice
else :
    print(" Invalid choice ")
    print("Please select 1,2, or 3 ")
print ()
print("                calculation completed                ")





