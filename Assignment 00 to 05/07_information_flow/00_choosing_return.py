ADULT_AGE = 18  # Legal adult age in the United States

def is_adult(age):
    return age >= ADULT_AGE

def main():
    age = int(input("How old is this person?: "))
    
    if is_adult(age):
        print("(Entered age is an adult age)")
    else:
        print("(Entered age is not an adult age)")
    
    print(is_adult(age))

# Call the main function
main()
