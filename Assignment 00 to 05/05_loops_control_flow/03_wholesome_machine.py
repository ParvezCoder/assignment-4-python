affirmation_sentence = "ok bro no issue"

def affirmation ():
    print("Please type the following affirmation: ", affirmation_sentence )

    user_affirmation = input()
    while affirmation_sentence != user_affirmation:
        print("That was not the affirmation.") 
        print("Please type the following affirmation: ", affirmation_sentence )
        user_affirmation = input()

    print("That's right! :)")


affirmation()