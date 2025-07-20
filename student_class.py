class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone_number(self):
        return self.__phone_number
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    def get_info(self):
        return (f"Name: {self.__name}\n"
                f"Address: {self.__address}\n"
                f"Age: {self.__age}\n"
                f"Phone Number: {self.__phone_number}\n")
person1 = Person("Thomas Sutters", "123 Maple Street", 30, "555-1234")
person2 = Person("Alice Wonderland", "456 Elm Avenue", 28, "555-5678")
person3 = Person("Bob Builder", "789 Oak Drive", 35, "555-9012")
print("Person 1 Info:\n" + person1.get_info())
print("Person 2 Info:\n" + person2.get_info())
print("Person 3 Info:\n" + person3.get_info())
