# Create an empty dictionary to store the counts
counts = {}

# Continuously ask for user input until they provide an empty input
while True:
    number = input("Enter a number: ")
    
    # If the input is an empty string, break out of the loop
    if number == "":
        break
    
    # Convert the input to an integer
    number = int(number)
    
    # Update the count in the dictionary
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

# After gathering all the numbers, print the counts
for number, count in counts.items():
    print(f"{number} appears {count} times.")
