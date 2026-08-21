# Topic 06: Loops
# Author Azmira khatun
#===============================

# Practice 1 : Print number 1 to 10
#=======================================

print (" =========== Practice :1 ===============")
for number in range ( 1,11 ) :
    print ( number )
print ()

# Practice 2 : Print number 10 to 1
#=======================================

print (" =========== Practice :2 ================")
for number in range( 10,0,-1):
    print ( number )
print ()

# Practice 3 : Print Even Number
print ("=========== Practice : 3 =================")
for number in range( 2,21,2):
    print (number )
print ()

# Practice 4 : Print Odd Numbers
print ("================== Practice :4 ======================")
for number in range(1,20,2):
    print(number)
print()

# Practice 5 : Sum from 1 to 100
print ("============ Practice : 5 ===========")
total = 0
for number in range ( 1,101):
    total = total + number
print("sum =",total)
print()


# Practice : 6 ,Sum of even numbers
print ("============== Practice : 6 =================")
total = 0
for number in range (2,101,2):
    total = total + number
print ("sum of even numbers =",total)
print()

# Practice 7: Multiplication Table
print ("============= practice :7 ==================")
number = int(input("Enter a number :"))
for multiplier in range (1,11):
    result = number * multiplier
    print (number,"x", multiplier ,"=",result )
print()


# practice 8: Multiplication Tables 1 to 5
for number in range (1,6):
    print()
    print("Table of",number )
for multiplier in range (1,11):
    result = number *  multiplier
    print (number,"x",multiplier,"=",result)
    print()

# practise 9 :Loop through a string

print ("=============== Practice : 9 ===============")
word = input ("Enter a word: ")
for character in word:
    print(character)
    print()


# Practice 10 : Count Character
print("================== Practice : 10 =================='")
word = input (" Enter a word:")
count = 0
for character in word :
    count = count + 1
print()


# Practice 11: Find Even AND ODD Number
print("===================== Practice : 11  =====================")
for number in range (1,21):
    if number % 2 == 0:
        print(number, "is even")
    else :
        print (number,"is odd")
print()

# Practice : 12: while Loop
print("================= Pracrice 12 ==============")
number = 1
while number<= 10:
    print(number)
    number = number +1
print()

# Practice 13 : Countdown Using While Loop
print("================= Practice : 13===================")
number = 10
while number >= 1:
    print(number)
    number = number - 1
print()

# Practice : 14 Sum using while loop
print("================ Practice : 14 ==================")
number = 1
total = 0
while number >= 100:
    total = total + number
number = number + 1
print("Sum =", total )
print()

# practice : 15 Free-fall distance calculation
print("================== Practice : 15=================")
print()
gravity = 9.81
time = int(input("Enter a time:(s)"))
for current_time in range(1,time+1):
    distance = 0.5*gravity*current_time**2
    print(
        "time=",
        current_time,
        "s| Distance =",
        round(distance,2),

    )
print()
print("================ All Practice Completed==========")

