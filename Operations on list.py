available_seats = list(range(1, 21))

while True:
    
    print("\nAvailable seats:")
    print(available_seats)

    try:
        choice = int(input("Enter the seat number you want to buy (0 to quit): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 20, or 0 to quit.")
        continue

    if choice == 0:
        print("Thank you for visiting! Enjoy your event.")
        break

    if choice < 1 or choice > 20:
        print("That seat number is out of range. Please choose between 1 and 20.")
    elif choice not in available_seats:
        print(f"Sorry, seat {choice} has already been sold. Please choose another.")
    else:
        available_seats.remove(choice)
        print(f"Seat {choice} has been successfully purchased.")

        if len(available_seats) == 0:
            print("All seats are sold out. Thank you!")
            break