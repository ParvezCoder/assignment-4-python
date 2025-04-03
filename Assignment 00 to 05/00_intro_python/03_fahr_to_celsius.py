def fahr_to_celsius():
    tem_fahr = int(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))
    tem_celsius = (tem_fahr-32) * 5.0/9.0
    print("Temprature:" + str(tem_fahr) + ".0F = " + str(tem_celsius) + "C")

if __name__ == "__main__":
    fahr_to_celsius()