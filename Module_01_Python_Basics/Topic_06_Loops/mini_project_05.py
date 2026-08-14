# Mini Project 05
# Physics Measurement Analyzer
# Topic 06 : Loops
# Author : Azmira Khatun
#===================================

# Student Information
#==============================

print("========================= Student Information=================")
student_name = input("Enter student name :")
print()
print("Welcome , ", student_name)
print()


# Experiment Information
#================================

print ("======================== Experiment Information=============")
experiment_name = input("Enter experiment name :")
initial_distance = float(input("Enter initial distance (m):"))
time_interval =float(input("Enter time_interval(s):"))
number_of_measurements = int(input("Enter number of measurements :"))


# Validation
#===================================

if number_of_measurements <=0:
    print()
    print("Error : Number of measurements must be greater than zero")
else :
    print()
print("==========================")
print(" Measurement  Result ")
print()
print("measurement",
      "time (S)",
      "distance (m)",
      "Velocity(m/s)"
      )
print("==================================")


# Calculation Variables
#=====================================

total_velocity = 0
total_distance = 0



 # Measurement loop
 #====================================

for measurement in range (1, number_of_measurements + 1):
    time = (measurement *
 time_interval)
    distance = (initial_distance
+ ( 5* time ))
    velocity = (distance -
initial_distance)/time

    total_velocity = total_velocity + velocity
    total_distance = total_distance + distance

    print(
        measurement,
        "         ",
        round( time, 20),
        "         ",
        round( distance,2),
        "         ",
        round (velocity,2),
    )


#Average Calculations
#========================================

average_velocity = (
    total_velocity/
number_of_measurements
)

#============================================
# Finial Result
#============================================

print()
print("====================================================")
print("  Final Result")
print("====================================================")

print(
    "total distance :, ",
    round(total_distance,2),
)
print(
    "Average velocity :",
    round(average_velocity,2),

)


#========================================
# Personal Analysis

print()
print("==================Analysis =================")
if average_velocity >100:
    print("motion status :  High velocity")
elif average_velocity >50:
    print("motion staus : Moderate velocity")
else:
    print("motion status : Low velocity")

print()


print(" Experiment Completed")
print()
print("=================================================")
print (" End of the Project ")









