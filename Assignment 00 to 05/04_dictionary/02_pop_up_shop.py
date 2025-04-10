import sys
from colorama import Fore, Style, init

init(autoreset=True)  # Initialize colorama (autoreset to ensure no color overflow)


def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        while True:
            # Bold and colored input
            amount_bought = input(f"{Fore.GREEN}{Style.BRIGHT}How many {fruit_name} do you want to buy? (Press Enter to exit): ")
            
            if amount_bought == "":
                print(f"{Fore.RED}{Style.BRIGHT}❌ No input detected. Exiting the program.")
                print(f"Your total so far is: ${total_cost}")
                sys.exit()
            
            try:
                amount_bought = int(amount_bought)
                total_cost += (fruits[fruit_name] * amount_bought)  # Add to total
                break
            except ValueError:
                print(f"{Fore.RED}❌ Please enter a valid number.")

    print(f"Your total is: ${total_cost}")

main()
