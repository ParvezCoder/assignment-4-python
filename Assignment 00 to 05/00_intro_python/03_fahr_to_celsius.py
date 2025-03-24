def fahr_to_celsius():
    tem_fahr = int(input("Enter temperature in Fahrenheit: "))
    tem_celsius = (tem_fahr-32) * 5.0/9.0
    print("Temprature:" + str(tem_fahr) + ".0F = " + str(tem_celsius) + "C")

if __name__ == "__main__":
    fahr_to_celsius()