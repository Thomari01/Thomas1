def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second
def main():
    char_list = ['a', 'b', 'c', 'd', 'e']
    print("All possible two-letter combinations:")
    for combo in two_letter_combinations(char_list):
        print(combo)
main()
