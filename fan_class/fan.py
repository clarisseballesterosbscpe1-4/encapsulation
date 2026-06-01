class Fan:
    slow = 1
    medium = 2
    fast = 3
    def __init__(self, speed=SLOW, radius=5, color="Blue", on=FALSE):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on
    
