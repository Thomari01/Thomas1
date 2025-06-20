# Get numerical grade from the user
grade = int(input("Enter the numeric grade: "))

# Check if the grade is within a valid range
if grade < 0 or grade > 100:
    print("Error: Grade must be between 0 and 100.")
else:
    if grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    elif grade >= 60:
        letter = "D"
    else:
        letter = "F"

    # Display the letter grade
    print(f"The letter grade is: {letter}")