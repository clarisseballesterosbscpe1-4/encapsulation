class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = ""

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

my_pet = Pet()

name = input("Enter pet name: ")
animal_type = input("Enter pet animal type: ")
age_number = input("Enter age number: ")
age_unit = input("Enter unit (month/months/year/years): ")
pet_age = f"{age_number} {age_unit} old"

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(pet_age)

print("\nPet Information")
print("---------------")
print("Name:", my_pet.get_name())
print("Animal Type:", my_pet.get_animal_type())
print("Age:", my_pet.get_age())
print("---------------")
