import math
def main():
    AB: float = float(input("\033[1;3m Enter the length of AB: \033[0m "))
    AC: float = float(input(" \033[1;3m Enter the length of AC: \033[0m"))

    BC: float = math.sqrt(AB**2 + AC**2)
    print("The length of BC (the hypotenuse) is: " + str(BC))



if __name__ == '__main__':
    main()