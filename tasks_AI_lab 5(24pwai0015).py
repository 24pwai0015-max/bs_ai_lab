# AI Password Strength Checker Lite

attempts = 5

for attempt in range(1, attempts + 1):
    password = input(f"Attempt {attempt}: Enter your password: ")

    conditions = 0

    # Condition 1: Length
    if len(password) >= 8:
        conditions += 1

    # Condition 2: Digit
    if any(char.isdigit() for char in password):
        conditions += 1

    # Condition 3: Uppercase
    if any(char.isupper() for char in password):
        conditions += 1

    # Feedback
    if conditions == 0:
        strength = "Very Weak"
    elif conditions == 1:
        strength = "Weak"
    elif conditions == 2:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"Password Strength: {strength}")

    # Winning Condition
    if strength == "Strong":
        print(f"You created a strong password!")
        print(f"AI Training Level: Beginner → Intermediate")
        break

    # Remaining attempts
    remaining = attempts - attempt
    print(f"Remaining attempts: {remaining}")

# Losing Condition
else:
    print(f"Final Result: Password is not strong enough.")