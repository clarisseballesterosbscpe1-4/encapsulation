class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def get_year_model(self):
        return self.__year_model

    def get_make(self):
        return self.__make

<<<<<<< HEAD
car = Car(2024, "Toyota")
print("=" * 45)
print("🚗 CAR SPEED SIMULATOR 🚗")
print("=" * 45)
print(f"Car Model : {car.get_year_model()}")
print(f"Car Make  : {car.get_make()}")
print("=" * 45)

print("Accelerating...\n")

for count in range(5):
    car.accelerate()
    print(f"[{count+1}] Speed: {car.get_speed()} km/h")

print("\n🛑 Braking...\n")

for count in range(5):
    car.brake()
    print(f"[{count+1}] Speed: {car.get_speed()} km/h")

print("\n🏁 Trip Complete!")
print(f"Final Speed: {car.get_speed()} km/h")
print("=" * 45)
=======
>>>>>>> c9b7911 (fixed oop)
