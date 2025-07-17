def main():
    print("Welcome to the Simple Python Calculator!")
    print("You can add, subtract, multiply, or divide two numbers.")
    print("-------------------------------------------------------")
    while True:
        try:
           
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

          
            operation = input("Choose operation (+, -, *, /): ")

           
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2  
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue  

            print(f"Result: {result}")
            break  

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError:
            print("Oops! Cannot divide by zero. Try again.")

main()
