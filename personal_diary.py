def main():
    """
    A simple personal diary program that appends user input to a text file.
    Each entry includes a user-provided date, time, and diary content.
    """
    date = input("Enter the current date (e.g., July 27, 2025): ")
    time = input("Enter the current time (e.g., 7:30 PM): ")
    
    entry = input("Write your diary entry:\n")
    try:
        diary_file = open('diary.txt', 'a')
        diary_file.write(f"Date: {date}, Time: {time}\n")
        diary_file.write(entry + "\n")
        diary_file.write("\n")  
        diary_file.close()
        print("Diary entry saved successfully.")
    except Exception as e:
        print("An error occurred while saving your diary entry:", e)
main()
