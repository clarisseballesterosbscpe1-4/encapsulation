from pet import Pet

print("=" * 45)
print("🐾 PET PROFILE SYSTEM 🐾")
print("=" * 45)

my_pet = Pet()

name = input("🐶 Enter pet name: ")
animal_type = input("🐱 Enter pet animal type: ")
age_number = input("🎂 Enter age number: ")
age_unit = input("📅 Enter unit (month/months/year/years): ")
pet_age = f"{age_number} {age_unit} old"

my_pet.set_name(name)
my_pet.set_animal_type(animal_type)
my_pet.set_age(pet_age)

print("\n" + "=" * 45)
print("🐾 PET INFORMATION CARD 🐾")
print("=" * 45)
print(f"🐕 Name          :", my_pet.get_name())
print(f"🐾 Animal Type           :", my_pet.get_animal_type())
print(f"🎂Age         :", my_pet.get_age())
print("=" * 45)
print("!! PET PROFILE SUCCESSFULLY CREATED !!")