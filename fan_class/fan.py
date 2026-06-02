class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color="Blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def set_speed(self, speed):
        self.__speed = speed
    def set_radius(self, radius):
        self.__radius = radius
    def set_color(self, color):
        self.__color = color
    def set_on(self, on):
        self.__on = on

    def get_speed(self):
        return self.__speed
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    def get_on(self):
        return self.__on

#fan 1
fan_1 = Fan()
fan_1.set_speed(Fan.fast)
fan_1.set_radius(10)
fan_1.set_color("Yellow")
fan_1.set_on(True)
#display fan 1
print("Fan 1")
print("------")
print("Speed:", fan_1.get_speed())
print("Radius:", fan_1.get_radius())
print("Color:", fan_1.get_color())
print("On:", fan_1.get_on())
print("------")
#fan 2
fan_2 = Fan()
fan_2.set_speed(Fan.medium)
fan_2.set_radius(5)
fan_2.set_color("Yellow")
fan_2.set_on(False)
#display fan_2
print("\nFan 2")
print("------")
print("Speed:", fan_2.get_speed())
print("Radius:", fan_2.get_radius())
print("Color:", fan_2.get_color())
print("On:", fan_2.get_on())
print("------")


