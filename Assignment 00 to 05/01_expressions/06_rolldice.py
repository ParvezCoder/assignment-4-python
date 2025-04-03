import random
number_side: int = 6

def main():
    die1: int = random.randint(1, number_side)
    die2: int = random.randint(1, number_side)
    
    total: int = die1 + die2
    
    print("Dice have", number_side, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()
