import datetime  # Import the datetime module

def main():
    # Ask for the birth year, month, and day
    birth_year = int(input("What year were you born? "))
    birth_month = int(input("What month were you born? (1-12) "))
    birth_day = int(input("What day of the month were you born? (1-31) "))
    
    birthday = datetime.date(birth_year, birth_month, birth_day)
    print(f"\nYour birthday is: {birthday}")
    
    today = datetime.date.today()

    # Put the difference between today and the birthday
    age_days = (today - birthday).days  # Difference in days

    # Calculate years (approximate, since not all years have exactly 365 days)
    age_years = age_days / 365.25  # Using 365.25 to account for leap years
    
    age_months = age_years * 12
    
    age_weeks = age_days // 7
    
    age_hours = age_days * 24
    age_minutes = age_hours * 60
    
    print("\nTime since your birth:")
    print(f"Years: {age_years:.1f}")
    print(f"Months: {int(age_months)}")
    print(f"Weeks: {int(age_weeks)}")
    print(f"Days: {age_days}")
    print(f"Hours: {age_hours:,}")
    print(f"Minutes: {age_minutes:,}")

main()
