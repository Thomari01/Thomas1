def main():
    books = []
    print("Enter 10 book titles:")
    count = 0
    while count < 10:
        title = input(f"Enter title #{count + 1}: ")
        title = title.title()  
        books.append(title)
        count += 1
    books_sorted = sorted(books)
    print("\nSorted Book Titles:")
    for book in books_sorted:
        print(book)
main()
