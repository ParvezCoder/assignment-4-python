year = int(input("Enter Year: "))

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print(f"{year}  It's a Leap Year")    
        else:
            print(f"{year}  It's not Leap Year")
    else:
        print(f"{year}  It's a Leap Year")
else:
    print(f"{year}  It's not Leap Year")