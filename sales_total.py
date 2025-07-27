def main():
    try:
        total = 0.0
        count = 0
        with open('sales_totals.txt', 'r') as file:
            for line in file:
                number = float(line.strip())
                total += number
                count += 1
                print(f"{number:,.2f}")
        average = total / count if count > 0 else 0
        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")
    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found. Please download it from the provided link and place it in the script folder.")
    except ValueError:
        print("Error: The file contains data that is not a valid number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
