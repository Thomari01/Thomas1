def main(): 
    example_string = "Hello, Python programmers!"
    print("Iterating through the string:")
    for char in example_string:
        print(char)
    min_char = min(example_string)
    print("\nCharacter with the minimum ASCII value:", min_char)
    max_char = max(example_string)
    print("\nCharacter with the maximum ASCII value:", max_char)
    index_of_o = example_string.find('o')
    print("\nIndex of 'o':", index_of_o)
    char_list = list(example_string)
    print("\nConverting string to a list of characters:", char_list)
    count_o = example_string.count('o')
    print("\nCount of 'o' in the string:", count_o)
main()
