import calendar
from datetime import datetime
def main():
    # Enter the current year 
    current_year = datetime.now().year
    # Enter the birth month
    try:
        birth_month = int(input("Enter your birth month (1-12): "))
        # Check if the month is within the valid range
        if 1 <= birth_month <= 12:
            # Set Sunday as the first day of the week
            calendar.setfirstweekday(calendar.SUNDAY)
            # Calendar for the current year and birth month
            print("\nHere is your birth month calendar:")
            print(calendar.month(current_year, birth_month))
        else:
            print("Error: Month must be between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 12.")
if __name__ == "__main__":
    main()
