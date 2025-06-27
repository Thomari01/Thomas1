names = []
for i in range(5):
    name = input(f"Enter name #{i + 1}: ")
    names.append(name.lower())  
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True
print("Sorted names (A to Z):")
print(names)
names.reverse()
print("Reversed names (Z to A):")
print(names)