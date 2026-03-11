# Task 1 – Basic Function and Function Call
def welcome_message():
    print("Welcome to Python Programming Lab")

welcome_message()


# Task 2 – Function with Parameters and Return
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(f"Sum: {result}")


# Task 3 – Function Call Stack Concept
def functionB():
    print("Inside Function B")

def functionA():
    print("Inside Function A")
    functionB()

functionA()


# Task 4 – Default Parameters
def greet(name="Student"):
    print(f"Hello {name}")

greet()          # Uses default
greet("Alice")   # Uses provided name


# Task 5 – Variable Scope
x = 10  # global variable

def scope_example():
    print(f"Global x inside function: {x}")
    y = 20
    print(f"Local y inside function: {y}")

scope_example()
# print(y)  # This would cause an error because y is local to the function


# Task 6 – Variable Length Arguments (*args)
def total_numbers(*numbers):
    return sum(numbers)

print(f"Total = {total_numbers(2, 3, 4, 5)}")
print(f"Total = {total_numbers(10, 20, 30)}")


# Task 7 – Keyword Variable Arguments (**kwargs)
def student_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

student_info(name="Arsalan", roll=101, course="Python", marks=95)


# Task 8 – Lambda Function
square = lambda n: n ** 2
print(f"Square of 6 = {square(6)}")


# Task 9 – Lambda with List
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print(f"Squares: {squares}")


# Task 10 – Lambda with Filter
marks = [45, 67, 82, 30, 90, 55]
high_marks = list(filter(lambda m: m > 50, marks))
print(f"Marks greater than 50: {high_marks}")