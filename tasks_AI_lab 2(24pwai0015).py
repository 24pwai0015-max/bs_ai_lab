# Task-01
full_name = input("Enter your full name: ")
favorite_color = input("Enter your favorite color: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year

print(f"Welcome, {full_name}!")
print(f"Your favorite color is {favorite_color} – perfect for calm AI thinking.")
print(f"You were born in {birth_year} → you are currently {age} years old ({current_year}).")

# Task-02
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /, **, %): ")

if operator not in ["+", "-", "*", "/", "**", "%"]:
    print("Invalid operator!")
else:
    if operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result:.2f}")
    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result:.2f}")
    elif operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "%":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")

# Task-03A
start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

current = start
while current <= end:
    if current % 7 == 0:
        current += 1
        continue
    if current % 2 == 0 and current % 5 == 0:
        print(f"{current}: Even & Multiple of 5!!")
    elif current % 2 == 0:
        print(f"{current}: Even")
    elif current % 5 == 0:
        print(f"{current}: Multiple of 5!")
    current += 1

# Task-03B
password = input("\nEnter a password to check strength: ")
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if len(password) < 6:
    print("Too short!")
elif not has_digit:
    print("Add at least one number")
elif not has_upper:
    print("Add at least one capital letter")
else:
    print("Strong password – good choice!")