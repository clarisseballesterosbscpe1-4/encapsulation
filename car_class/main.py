from car import Car

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