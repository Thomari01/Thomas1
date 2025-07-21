class NotNumericError(Exception):
    """Exception raised when input is not numeric."""
    def __init__(self, input_value, message="Input is not a number."):
        self.input_value = input_value
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"'{self.input_value}' -> {self.message}"
def get_number():
    while True:
        try:
            user_input = input("Enter a number: ")
            if not user_input.isnumeric():
                raise NotNumericError(user_input)
        except NotNumericError as e:
            print(f"Error: {e}")
        else:
            print(f"Success: You entered the number {user_input}")
            break  
        finally:
            print("Attempt complete.\n")
if __name__ == "__main__":
    get_number()
    print("Program has ended.")
