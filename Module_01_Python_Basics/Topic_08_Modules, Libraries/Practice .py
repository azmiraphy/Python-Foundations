#========================================
# Topic 08 : Modules and Libraries
# Practice
# Author : Azmira Khatun
#=========================================


# Practice : Import math
#===================================================
print("========================= practice 01 ====================")
import math
number = 25
result = math.sqrt(number)
print("Square root =", result)

#Practice : Math Constants
#====================================================
print("========================== Practice 02 =======================")
print("Value of pi =", math.pi)


#====================================================
# Practice : Power using math
print("========================== Practice 03 =======================")
base = 2
power = 5
result = math .pow (base , power)
print("Result =",result)

#=====================================================
# Practice : Trigonometric Functions
print("========================== Practice 04 =======================")
angle = 30
angle_in_radians = math. radians(angle)
sin_value = math.sin(angle_in_radians)
cos_value = math . cos (angle_in_radians)
print ("sin (30)=", sin_value)
print("cos(30)=",cos_value)

#=======================================================
# Practice : From module import
print("============================ Practice 05===========================")
from math import sqrt,pi
radius = 5
area = pi* radius ** 2
print("Radius =", radius)
print("Area = ", area)
print("Square root of 100 =", sqrt(100))


#===========================================================
# Practice : Module Alias
print("========================== Practice 06 ==========================")
import math as m
number = 16
print("square root =",m.sqrt(number))


#===========================================================
#Practice : Random Module
print("========================== practice 07 ===========================")
import random
random_number = random.randint(1,100)
print("random number =",random_number)

#=========================================================
#Practice : physics calculation with math
print("============================== Practice 08=====================")
mass = 5
velocity =10
kinetic_energy = .5*mass * velocity **2
print("mass =",mass ,"kg")
print("velocity =",velocity,"m/s")
print("kinetic_energy=",kinetic_energy,"J")


#==========================================================
# Practice : Projectile Component
print("========================== Practice 09======================")
velocity = 20
angle = 45
angle_in_radius = math. radians(angle)
horizontal_velocity = (
    velocity * math .cos(angle_in_radians)

)
vertical_velocity = (
    velocity * math .sin(angle_in_radians)
)
print("horizontal_velocity =",
      round(horizontal_velocity,2),
      "m/s"
      )
print(
    "Vertical velocity =",
    round(vertical_velocity,2),
    "m/s"
)

#==================================================
# Practice : Create Own Module
print("======================== Practice 10=========================")
print(" create a separate Python file named:")
print(" physics_tools .py")
print()

print (" inside that file , create functions such as:")
print("calculate_velocity()")
print("calculate_force()")
print("calculate_acceleration()")
print("kinetic_energy()")
print()
print(" then import that module into another Python file ")

print()
print("=============== Practice Completed ================")


