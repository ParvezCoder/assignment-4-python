# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16.
#  You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua
#  where the voting age is 48.

take_age = int(input("\033[94mHow old are you \033[0m"))

if take_age >= 16 and take_age <= 25:
    print("""you can vote in Peturksbouipo where the voting age is 16.
You cannot vote in Stanlau where the voting age is 25.
You cannot vote in Mayengua where the voting age is 48.""")
elif take_age >= 26 and take_age <= 47:
    print(""" You can vote in Stanlau where the voting age is 25.
you cannot vote in Peturksbouipo where the voting age is 16
You cannot vote in Mayengua where the voting age is 48.""")

elif take_age >= 48 and take_age <= 80:
    print(""" You can vote in Mayengua  where the voting age is 48.
you cannot vote in Peturksbouipo where the voting age is 16
You cannot vote in  Stanlau where the voting age is 25.""")
