class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color="Blue", on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on

    def set_speed(self, speed):
        self.speed = speed
    def set_radius(self, radius):
        self.radius = radius
    def set_color(self, color):
        self.color = color
    def set_on(self, on):
        self.on = on

    def get_speed(self):
        return self.speed
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_on(self):
        return self.on

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

