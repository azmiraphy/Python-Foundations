#=========================
# Topic 05 : Conditional Statements
# Author : Azmira Khatun
#=====================================

print("============== Practice 1: Positive or Negative==============")
number = float(input("Enter a number :"))
if number > 0:
    print("positive Number")
elif number < 0:
    print("Negatibe Numbber")
else:
    print("Zero")
print()


print("============== Practice 2: Even or Odd ===============")
number = int(input("Enter a number :"))
if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
print()

print("============== Practice 3: pass or fail===============")
marks = float(input("Enter your marks :"))
if marks >= 50:
    print("pass")
else:
    print("fail")
print()


print("================== Practice 4 : Largest of Two Numbers ============")
a = float(input("Enter first number : "))
b = float(input("Enter secind number :"))
if a>b:
    print("Largest=",a)
else:
    print("Largest=",b)
print()


print("============== Practice 5 : Largest of Three Numbers=============")
a = float(input("Enter first number :"))
b = float(input("Enter second number :"))
c =  float(input("Enter third number :"))
if a>=b and a>=c :
    print("largest=",a)
elif b>=a and b>=c :
    print("largest= b",b)
else:
    print("largest= c",c)
print()


print("================ Practice 6 : Age Checker============")
age = int(input("Enter your age :"))
if age >= 18 :
    print(" you are eligible  to vote.")
else :
    print(" you are not eligible to vote.")
print()


print("================= Practice 7 : Password Checker =============")
password = input("Enter your password :")
if password ==  "physics123" :
    print ("login successful")
else :
    print("Incorrect password")
print()


print("================ Practice 8 : Grade Calculator ==============")
marks = float(input("Enter marks :"))
if marks >= 80:
    print("Grade : A+")
elif marks >= 70:
    print("Grade : A")
elif marks >= 60:
    print("Grade : A-")
elif marks >= 50:
    print("Grade : B")
else:
    print("Grade : F")
print()

print("================= Practice 9 : Temperature Condition =============")
temperature = float(input("Enter temperature :"))
if temperature >= 40 :
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature>= 20 :
    print("Normal")
else:
    print("Cold")
print()

print("================ Practice 10 : Leap year checker============")

year = int(input("Enter year :"))
if (year %  400 == 0 ) or (year % 4 == 0 and year % 100 !=0):
    print("Leap Year")
else:
    print("Not a Leap Year")




