#===================================
# Mini Project 04
# Physics Lab Eligibility System
# Author : Azmira Khatun
#===========================================

print("======================================")
print("Physics lab eligibility system")
print("=====================================")

student_name = input("Enter Student name:")
attendance = float(input("Attendance(%):"))
lab_marks = float(input("lab marks (50):"))
theory_marks = float(input("theory marks (50):"))
total = lab_marks+theory_marks
print()

if attendance >=75:
    print("attendance status: Eligible")
else:
    print("attendance status : Not eligible")
print()
if total >=90:
    grade = "A+"
elif total>=80:
    grade = "A"
elif total >=70:
    grade = "A-"
else:
    grade = "F"
print("Grade:",grade)
print()

if attendance >=75 and total >=60:
    print("Final result : Pass")
else:
    print("Final result :Fail")


