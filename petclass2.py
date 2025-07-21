class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name
    
    def get_kind(self):
        return self.__kind
    def get_breed(self):
        return self.__breed
    def get_name(self):
        return self.__name
    def set_kind(self, kind):
        self.__kind = kind
    def set_breed(self, breed):
        self.__breed = breed
    def set_name(self, name):
        self.__name = name
    
    def print_details(self):
        print("----- Pet Details -----")
        print(f"Kind : {self.__kind}")
        print(f"Breed: {self.__breed}")
        print(f"Name : {self.__name}")
        print("------------------------\n")

pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Mittens")
pet3 = Pet("Bird", "Parrot", "Kiwi")

pet1.print_details()
pet2.print_details()
pet3.print_details()

print(f"Class name using __name__: {Pet.__name__}")

print(f"Type of pet1 object: {type(pet1)}")

print(f"Module name of Pet class: {Pet.__module__}")

print(f"Base classes of Pet: {Pet.__bases__}")

print(f"Is pet2 an instance of Pet? {isinstance(pet2, Pet)}")
print(f"Is pet3 an instance of str? {isinstance(pet3, str)}")  # Should be False
