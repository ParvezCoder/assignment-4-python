day_in_year: int = 365
hours_in_day: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    print("There are " + str(day_in_year * hours_in_day * MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")



if __name__ == '__main__':
    main()