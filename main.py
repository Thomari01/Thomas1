# main.py
from employee import ProductionWorker
def main():
    print("Enter the following details of the Employee")
    print("--------------------------------------------")
    
    name = input("Enter Employee Name: ")
    number = input("Enter Employee Number: ")
    pay_rate = float(input("Enter Pay Rate: "))
    shift_number = int(input("Enter Shift Number (1 for Day, 2 for Night): "))
    
    worker = ProductionWorker(name, number, shift_number, pay_rate)

    print("-------------------------------------------------------")
    print("Details of Employee:")
    print("-------------------------------------------------------")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_number())
    
    if worker.get_shift_number() == 1:
        shift_text = "Day"
    elif worker.get_shift_number() == 2:
        shift_text = "Night"
    else:
        shift_text = "Unknown"

    print("Shift:", shift_text)
    print("Pay Rate:", worker.get_pay_rate())

if __name__ == "__main__":
    main()
