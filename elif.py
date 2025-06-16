# Prompt the user to enter a numeric grade
grade_input = input("Enter the numeric grade: ")

# Check if the input is a number and within 0 to 100
if grade_input.replace('.', '', 1).isdigit():  # Allows integer or decimal input
    grade = float(grade_input)
    
    if 0 <= grade <= 100:
        # Determine the letter grade using elif statements
        if grade >= 90:
            letter_grade = 'A'
        elif grade >= 80:
            letter_grade = 'B'
        elif grade >= 70:
            letter_grade = 'C'
        elif grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        # Display the result in the requested format
        print(f"The letter grade is: {letter_grade}")
    else:
        print("❌ Please enter a number between 0 and 100.")
else:
    print("❌ Invalid input. Please enter a numeric grade.")