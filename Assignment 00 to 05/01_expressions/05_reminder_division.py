def reminder_division():
    divident = int(input(" \033[1;3m Please enter an integer to be divided: \033[0m "))
    divisor = int(input("  \033[1;3m Please enter an integer to divide by: \033[0m"))
    qos = divident // divisor
    remi = divident % divisor
    print("The result of this division is ",qos," with a remainder of ",remi)

if __name__ == "__main__":
    reminder_division()