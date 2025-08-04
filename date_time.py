from datetime import datetime

def main():
    year = int(input("What year were you born?  "))
    month = int(input("What Month were you born (as a number. May would be 5)  "))
    day = int(input("What day of the month were you born?  "))

    birthday = datetime(year, month, day)

    # Print the birthday in YYYY-MM-DD format
    print("Your birthday is: ")
    print(birthday.date())

    # Get today's current date and time
    today = datetime.now()

    # Calculate the difference between today and birthday
    difference = today - birthday

    total_days = difference.days
    print(f"The difference is {total_days} days")

    age_years = round(total_days / 365, 1)  
    print(f"You are {age_years} years old")

if __name__ == "__main__":
    main()
