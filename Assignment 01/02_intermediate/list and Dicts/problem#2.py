def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return "Element updated successfully!"
    else:
        return "Index out of range!"

def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 < end <= len(my_list) and start < end:
        return my_list[start:end]
    else:
        return "Invalid start or end index!"

def play_game():
    my_list = ['cat', 'dog', 'fish', 'bird', 'lion']

    while True:
        print("\nYour list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice! Try again.")

# Start the game
play_game()
