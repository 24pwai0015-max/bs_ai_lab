import random

# Game Setup
secret_number = random.randint(1, 50)
attempts = 7

print(f"🎮 Welcome to AI Number Guessing Game Lite!")
print(f"Guess a number between 1 and 50. You have {attempts} attempts.\n")

# Game Loop
for attempt in range(1, attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        # Input Validation
        if guess < 1 or guess > 50:
            print(f"⚠️ Please enter a number between 1 and 50.")
            continue

        # Check Guess
        if guess > secret_number:
            print(f"📉 Too high!")
        elif guess < secret_number:
            print(f"📈 Too low!")
        else:
            print(f"🎉 You win in {attempt} attempts!")

            # AI Training Level
            if attempt <= 3:
                level = "Intermediate"
            else:
                level = "Beginner → Intermediate"

            print(f"🤖 AI training level: {level}")
            break

        # Remaining attempts
        remaining = attempts - attempt
        print(f"⏳ Remaining attempts: {remaining}\n")

    except ValueError:
        print(f"❌ Invalid input! Please enter an integer.\n")

# If player loses
else:
    print(f"💀 Game Over! The correct number was {secret_number}.")
