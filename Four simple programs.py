def main():
    import re  
    symbol_set = "!@#$%&*"
    while True:
        try:
            password = input("Enter a password: ")
        
            if len(password) < 8 or len(password) > 20:
                print("Password must be between 8 and 20 characters.")
                continue
            
            if not any(char.isupper() for char in password):
                print("Password must contain at least one uppercase letter.")
                continue
            if not any(char.islower() for char in password):
                print("Password must contain at least one lowercase letter.")
                continue
            if not any(char.isdigit() for char in password):
                print("Password must include at least one number.")
                continue
            if not any(char in symbol_set for char in password):
                print(f"Password must include at least one symbol from: {symbol_set}")
                continue
           
            confirm = input("Confirm your password: ")
            if password == confirm:
                print("Password successfully set!")
                break
            else:
                print("Passwords do not match. Please try again.\n")
        except Exception as e:
            print(f"An error occurred: {e}")
main()
