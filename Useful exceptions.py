def modify_artist_list(top_artists):
    try:
        print("\nCurrent Top Performing Artists:")
        for i, artist in enumerate(top_artists):
            print(f"{i}: {artist}")
        
        index_input = input("\nEnter the index number (0–9) of the artist you want to replace: ")
        index = int(index_input)  

        new_artist = input("Enter the new artist's name: ")
        top_artists[index] = new_artist  

        print("\nArtist updated successfully!")
        print("Updated Artist List:")
        for i, artist in enumerate(top_artists):
            print(f"{i}: {artist}")

    except (ValueError, IndexError):
        print("An input error occurred. Please enter a valid number and ensure the index is within range (0–9).")


def main():
    top_artists = [
        "The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
        "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"
    ]
    modify_artist_list(top_artists)
main()
