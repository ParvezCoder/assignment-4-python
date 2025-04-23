import random

NUM_ROUNDS = 5
score = 0

print("Welcome to the High-Low Game!")
print("--------------------------------")

for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate random numbers
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"Your number is {user_number}")
    
    # Get user guess with input validation
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").strip().lower()

    # Determine result
    correct = False
    if guess == "higher" and user_number > computer_number:
        correct = True
    elif guess == "lower" and user_number < computer_number:
        correct = True

    if correct:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}\n")

print("Thanks for playing!")
