sentence: str = "Panaversity is fun. I learned to program and used Python to make my " 
def main():
    adjective: str = input(" \033[1;3m Please type an adjective and press enter. \033[0m ")
    noun: str = input(" \033[1;3m Please type a noun and press enter. \033[0m")
    verb: str = input(" \033[1;3m Please type a verb and press enter. \033[0m")

    print(sentence + adjective + " " + noun + " " + verb + "!")



if __name__ == '__main__':
    main()