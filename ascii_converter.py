def main():
    user_input = input("Enter a single character: ")
    if len(user_input) != 1:
     print("Error: You must enter exactly one character.")
    else:
     ascii_value = ord(user_input)
    print(f"The ASCII value of '{user_input}' is {ascii_value}.")
    try:
        ascii_input = int(input("Enter an ASCII value (32 to 127): "))
        if 32 <= ascii_input <= 127:
            character = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is '{character}'.")
        else:
            print("Error: Value must be between 32 and 127.")
    except ValueError:
        print("Error: You must enter a valid integer.")
if __name__ == "__main__":
    main()
