# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!
def tall():
    while True:
        user_input = input("How tall are you? (press Enter to quit): ")
        if user_input == "":
            break  # Exit the loop

        height = int(user_input)  # Convert only after checking it's not empty

        if height >= 50:
            print("You're tall enough to ride! 🎢")
        else:
            print("You're not tall enough to ride, but maybe next year! 🚫")

tall()
