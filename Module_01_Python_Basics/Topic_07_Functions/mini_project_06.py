# ==================================
# Mini Project 06 : physics Formula calculator
# Topic 07 : Functions
# Author : Azmira Khatun

# Function 01 : Calculate Velocity
#===================================================

def calculate_velocity(distance,time):
    if time <= 0:
        return None
    return distance/time


# Function 02 : calculate acceleration
#================================================

def calculate_acceleration(initial_velocity,final_velocity, time):
    if time<=0:
        return None
    return(final_velocity-initial_velocity)/time


#Function 03 : Calculate Force
#=================================================
def calculate_force(mass , acceleration):
    return mass * acceleration


# Function 04: Calculate_ kinetic_energy
#==================================================
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity **2


# Function 05 : calculate potential Energy
#====================================================
def calculate_potential_energy(mass, height):
    gravity = 9.81
    return  mass * gravity * height

# Function 06: Display Result
#====================================================
def display_result(name, value, unit):
    print(name,"=",round(value,2),unit)



# Main Program
#====================================================
print("===============================================")
print("                PHYSICS FORMULA  CALCULATOR              ")
print("===============================================")
print()
print("Avaiable calculations :")
print("1 . Velocity ")
print("2 . Acceleration ")
print("3 . Force ")
print("4 . Kinetic Energy ")
print("5 . Potential Energy ")
print()

choice = int(input("Enter your choice (1-5)"))
print()


# Velocity
#===========================================
if choice == 1 :
    distance = float(input("Enter distance(m):"))
    time = float(input("Enter time(s)"))
    velocity = calculate_velocity(distance,time)
    if velocity is None :
        print("Error : time must be greater than zero .")
    else :
        display_result(
            "velocity = ",velocity,"m/s"
        )


 # ================================================
 # Acceleration
elif choice == 2 :
    initial_velocity = float(input("Enter initial velocity(m/s)"))
    final_velocity = float(input("Enter final velocity(m/s)"))
    time = float(input("Enter time (s):"))

    acceleration = calculate_acceleration(
        initial_velocity,
        final_velocity,
        time
    )
    if acceleration is None :
        print("Error : time must be greater than zero .")
    else:
        display_result(
            "acceleration",
            acceleration,
            "m/s^2"
        )


#========================================================
# Force
elif choice ==3 :
    mass = float(input("Enter mass (kg):"))
    acceleration = float(
        input("enter acceleration (m/s^2):")

    )
    force = calculate_force(
        mass ,
        acceleration
    )
    display_result(
        "force",
        force,
        "N"
    )


#============================================
# Kinetic Energy
#============================================

elif choice == 4 :
    mass = float(input("Enter mass (kg):"))
    velocity = float(input("Enter velocity(m/s):"))
    kinetic_energy = calculate_kinetic_energy (
        mass,
        velocity
    )
    display_result(
        "kinetic energy",
        kinetic_energy,
        "J"

    )


#=====================================================
# Potential Energy
#=====================================================
elif choice == 5 :
    mass = float(input("Enter mass (kg):"))
    height = float(input("Enter height(m):"))
    potential_energy = calculate_potential_energy(
        mass,
        height
    )
    display_result(
        "potential Energy ",
        potential_energy,
        "j"

    )

#==================================================
# Invalid Choice
else:
    print("invalid choice .")
    print(" please select a number from 1 to 5 .")

    print()
    print("                Calculation Completed                ")
    print("========================================================")