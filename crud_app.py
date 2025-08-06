def main_menu():
    print("Menu:")
    choice = 0
    while not (1 <= choice <= 5):
        try:
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

def main():
    choice = 0
    while choice != 5:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
    print("\nData saved as customer_list.txt\n")

def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

def read():
    customers = check()
    search_lname = input("Enter the last name of the customer to find: ").strip().lower()
    found = False
    for line in customers:
        if search_lname in line.lower():
            print("Entry found:", line.strip())
            found = True
    if not found:
        print("No entry found with that last name.")

def update():
    customers = check()
    search_lname = input("Enter the last name of the customer to update: ").strip().lower()
    updated = False
    for i in range(len(customers)):
        if search_lname in customers[i].lower():
            print("Current Entry:", customers[i].strip())
            fname = input("Enter new first name: ")
            lname = input("Enter new last name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            customers[i] = f"{fname}, {lname}, {phone}, {email}\n"
            updated = True
            break
    if updated:
        save(customers)
        print("Entry updated.")
    else:
        print("No entry found with that last name.")

def delete():
    customers = check()
    search_lname = input("Enter the last name of the customer to delete: ").strip().lower()
    new_list = []
    deleted = False
    for line in customers:
        if search_lname not in line.lower():
            new_list.append(line)
        else:
            print("Deleting entry:", line.strip())
            deleted = True
    if deleted:
        save(new_list)
        print("Entry deleted.")
    else:
        print("No entry found with that last name.")

if __name__ == "__main__":
    main()
