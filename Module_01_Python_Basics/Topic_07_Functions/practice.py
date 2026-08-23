# Topic 07 : Functions
#Auhtor : Azmira Khatun


#Practice 01: Basic function
print("====================== Practice 01===============")
def greet():
    print("HELLO, welcome to python functions")
    greet()

#pracrice 02: function with a perameter
print()
print("============== practice 02===============")
def greet_user(name):
    print("hello",name)
greet_user("Azmira")


#practice 03 : function with two parameters
print()
print("============= Practice 03 ===============")
def add_numbers(a,b):
    print("sum=",a+b)
add_numbers(10,20)

# practice 04 : Function with return
print("================== Practice 04 ================")
def add_numbers(a,b):
    return a+b
result = add_numbers(10,20)
print("result =",result)

#practice 05:  Subtraction function
print()
print("============== Practice 05 ===============")
def subtract_numbers(a,b):
    return a-b
result = subtract_numbers(70,20)
print("Difference =",result)

# practice 06 : Multiplication Functions
print("=====================  practice 06 ===================")
def multiply_numbers(a,b):
    return a*b
result= multiply_numbers(10,9)
print("Multiplication =:", result)

#practice 07:  Division Function
print()
print("================ Practice 07 ================")
def divide_numbers(a,b):
    if b == 0:
        return " Cannot divide by zero ."
    return a/b
result = divide_numbers(10,9)
print("division =", result)

#practice 08: positive, negative or zero
print()
print("================ practice 08 ================")
def check_even_odd(numbers):
    if numbers % 2 == 0:
        return"Even"
    return"Odd"
result = check_even_odd(15)
print("Numbers is ",result)


#Practice 9: Positive , Negative or Zero
print()
print("================ Practice 09 ================")
def check_number(numbers):
    if numbers > 0:
        return"Positive"
    elif numbers < 0 :
        return"Negative"
    return "Zero"
result = check_number(-8)
print("Numbers is", result)


#  Practice 10 : Square Function
print()
print("================ Practice 10 ================")
def square (numbers):
    return numbers**2
result = square (7)
print("Square =",result)


# practice 11 : Cube Function
print()
print("================ Practice 11 ===============")
def cube (numbers):
    return numbers**3
result = cube(4)
print("Cube = ", result)


# practice 12 : Function with use Input
print()
print("================= Practice 12 ===============")
def calculate_square(numbers):
    return number**2
number = float(input("Enter a number :"))
result = calculate_square( number)
print("square =",result)


# practice 13 : default Parameter
print()
print("================ practice 13 ===============")
def introduce(name,
country = "Bangladesh"):
    print("Name:",name)
    print("country:",country)
introduce("Azmira")
print()
introduce("Sara,Malaysia")



# PRACTICE 14:Keyword Arguments
print("================ Practice 14=============")
def student_information(name,
department,university):
     print("name:",name)
     print("department:",department)
     print("University:",university)

student_information(name ="zara",
                    department = "physics",
                    university = "National University"
                    )


# Practice 15 : Function with Loops
print()
print("================ Practice 15 ===============")
def print_numbers(start, end):
    for numbers in range (start,end+1
):
        print(number)
print_numbers(1,10)


# practice : 16 Sum using a Function and  Loop
print()
print("================= Practice 16 =============== ")
def calculate_sum(start,end ):
    total = 0
    for numbers in range (start, end+
1):
        total = total + number
    return total
result = calculate_sum(1,100)
print ("sum = ", result)

# practice 17 : Factorial function
print()
print("================ Practice 17 ===============")
def factorial (numbers):
    results = 1
    for value in range (1,numbers +1):
        results = result * value
    return result
number = int( input("Enter a positive integer :"))
if number >=0:
    print("Factorial=",factorial (number))
else :
    print ("factorial is not defined for negative numbers.")


# practice 18 : Average function
print()
print("================ Practice 18 ================")
def calculate_average(numbers):
    if len(numbers)==0:
        return 0
    total = 0
    for number in numbers :
        total = total +number
    return total/len (numbers)
values = [ 10,20,30,40,50]
average = calculate_average(values)
print("Average = ", average)

# practice 19 : Physics velocity Function
print()
print("================ Practice 19 ===============")
def calculate_velocity (distance , time):
    if time <=0 :
        return "time must be greater than zero"
    return distance/time
distance = float(input("Enter distance (m):"))
time = float (input("Enter time (s)"))
velocity = calculate_velocity (distance,time)
print("velocity =",velocity,"m/s")

print("===================== ALL Practices Completed=============")










