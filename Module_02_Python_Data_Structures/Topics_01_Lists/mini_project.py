# Mini Project 01 : Solar Energy Data Analyzer
# Module 02 - Python Data structures
# Topic 01 - Lists
# Author : Azmira Khatun
#====================================================

# 1. Solar Energy Data
#------------------------------------
solar_energy = [
    120,
    150,
    135,
    180,
    200,
    175,
    220,
    250
]
days = [
    "Day 1",
    "Day 2",
    "Day 3",
    "Day 4",
    "Day 5",
    "Day 6",
    "Day 7",
    "Day 8"
]

print("solar energy length:",len(solar_energy))
print("days length :",len(days))
# 2. Total Energy Production
#-------------------------------------
total_energy = sum(solar_energy)
print("\ntotal Energy Production:",total_energy,"KWh")

# 3. Average Energy Production
#---------------------------------------
average_energy = total_energy / len(solar_energy)
print("Average Daily Production :",round(average_energy,2),"kwh")


# 4 . Maximum Energy Production
#---------------------------------------
maximum_energy = max (solar_energy)
maximum_index = solar_energy .index(maximum_energy)
print(
    "Maximum Energy Production:",solar_energy,
    "KWh",
    days[maximum_index]

)

# 6. Minimum Energy Production
#--------------------------------------
minimum_energy = min(solar_energy)
minimum_index = solar_energy.index(minimum_energy)
print("minimum energy:",solar_energy,"kwh",
      days[minimum_index]
      )

# 7. High Production days
#------------------------------------
threshold = 180
high_production = [
    energy for energy in solar_energy
    if energy >= threshold
]
print("\nHigh Production values :",high_production)



# Sorted Data
#-----------------------------------
ascending_data = sorted(solar_energy)
print("\nAscending Order :")
descending_data = sorted(
    solar_energy,
    reverse = True
)
print("\ndescending order :")
print(descending_data)


# Data Summary
#---------------------------------------
print("\n"+ "=" * 50)
print("   data summary   ")
print("=" * 50)
print(f"Number of days     :{len(solar_energy)}")
print(f"total energy  : {total_energy}KWh")
print (f" average energy : {average_energy :.2f} Kwh")
print(f" maximum energy : {maximum_energy } Kwh")
print(f" minimum energy : {minimum_energy}kwh")
print ("=" *50)
print("Analysis Compled successfully")
print("=" * 50)

