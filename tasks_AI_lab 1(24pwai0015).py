print("muhammad arsalan\n24pwai0015\nprogramming for Ai lab 1")
# part 1
name = "Arslan"
age = 20
city = "Lahore"

# Printing variables
print("Name:", name)
print("Age:", age)
print("City:", city)

# Number variables
num1 = 10
num2 = 5

print("Sum:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("div:", num1 / num2)


# ////////////////////////////////////////////////////////////////////////////////




# PART 2 – Input and Output

MY_name = input("Enter your name: ")
MY_age = int(input("Enter your age: "))

print("Hello", MY_name + ", you are", MY_age, "years old")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("div:", number1 / number2)

# ////////////////////////////////////////////////////////////////////////



# PART 3 – Comments


# This program demonstrates basic Python concepts
# It takes user input and performs calculations
# It also checks conditions and loops
# lets talk about advance libraries 

"""
This is a multi-line comment.
The program includes variables, input/output,
conditions, loops, functions, and type checking.

"""

# ///////////////////////////////////////////////////////////////////


# PART 4 – Type Check

a = 10
b = 3.14
c = "Python"
d = True

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

# ////////////////////////////////////////////////////////////////////


# PART 5 – Data Type

age_input = int(input("Enter your age: "))
print("After 10 years, you will be:", age_input + 10)

marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

average_marks = (marks1 + marks2 + marks3) / 3

print("Average marks:", average_marks)

# /////////////////////////////////////////////////////////////////////


# part - 6 CONDITIONS

# Task 1 – Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 2 – Grade System

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Task 3 – Voting Eligibility
vote_age = int(input("Enter your age for voting check: "))

if vote_age >= 18:
    print("You can vote")
else:
    print("Not eligible")


# Task 4 – Print Numbers (For Loop)
for i in range(1, 11):
    print(i)


# Task 5 – Multiplication Table
table_num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(table_num, "x", i, "=", table_num * i)


# Task 6 – Sum of First 10 Numbers
total = 0
for i in range(1, 11):
    total += i

print("Sum of first 10 numbers:", total)


# Task 7 – Password Checker
correct_password = "hell"
password = ""

while password != correct_password:
    password = input("Enter password: ")

print("Access Granted")


# Task 8 – Function
def average(a, b, c):
    return (a + b + c) / 3

print("Function Average:", average(10, 20, 30))