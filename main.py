import turtle
import time
import math

turtle.tracer(0, 0)
turtle.speed(0)

s = turtle.Screen()

DeltaTime = 0.1

G = 6.6743 * pow(10, -11)

class Vector :
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, b) :
        return Vector(self.x + b.x, self.y + b.y)

    def __mul__(self, b) :
        if (isinstance(b, Vector)) :
            return Vector(self.x * b.x, self.y * b.y)
        else :
            return Vector(self.x * b, self.y * b)
        
    
    def __truediv__(self, b) :
        if ((b.x != 0.0) & (b.y != 0.0)) :
            if (isinstance(b, Vector)) :
                return Vector(self.x / b.x, self.y / b.y)
            else :
                return Vector(self.x / b, self.y / b)
        else :
            if (b.x == 0.0) :
                return Vector(0, self.y / b.y)
            else :
                return Vector(self.x / b.x, 0)
    
    def __sub__(self, b) :
        return Vector(self.x - b.x, self.y - b.y)

    def __pow__(self, b) :
        i = 0
        while i < b :
            self = self * b
            i = i + 1
        
        return self


class Planet :
    name = ""
    acceleration = Vector(0, 0)
    velocity = Vector(0, 0)
    velocity = Vector(0, 0)
    radius = 0
    mass = 0.0

    def __init__(self, name, radius, mass, velocity = Vector(0, 0), position = Vector(0, 0)) :
        self.name = name
        self.velocity = velocity
        self.position = position
        self.radius = radius
        self.mass = mass

    def CalculateAttraction(self, b) :
        attraction = (Vector(G * self.mass * b.mass, G * self.mass * b.mass) / (pow(self.position - b.position, 2))) * -1

        print(self.name, " Distance to ", b.name,(self.position - b.position).x, (self.position - b.position).y)
        print(self.name, "Attraction to ", b.name,attraction.x, attraction.y)

        print("\n", "\n")

        return attraction

    def Tick(self, PlanetList) :
        i = 0
        while i < len(PlanetList) :
            if (PlanetList[i] != self) :
                self.acceleration = self.CalculateAttraction(PlanetList[i])
            i = i + 1
        self.velocity = Vector(math.floor(self.velocity.x + self.acceleration.x), math.floor(self.velocity.y + self.acceleration.y))
        self.position = Vector(math.floor(self.position.x + self.velocity.x), math.floor(self.position.y + self.velocity.y))

        if self.position.x < -s.window_width() / 2 :
            self.position.x = -s.window_width() / 2
        elif self.position.x > s.window_width() / 2 :
            self.position.x = s.window_width() / 2
        if self.position.y < -s.window_height() / 2 :
            self.position.y = -s.window_height() / 2
        elif self.position.y > s.window_height() / 2 :
            self.position.y = s.window_height() / 2  

Earth = Planet("Earth", 10, 100000)
Moon = Planet("Moon", 7, 700, Vector(10, 0), Vector(0, 70))

PlanetList = [Earth, Moon]

while True :
    time.sleep(DeltaTime)
    s.clearscreen()
    turtle.tracer(0, 0)
    turtle.speed(0)
    turtle.ht()
    i = 0
    while i < len(PlanetList) :
        print("Position of ", PlanetList[i].name, PlanetList[i].position.x, PlanetList[i].position.y)
        print("Velocity of ", PlanetList[i].name, PlanetList[i].velocity.x, PlanetList[i].velocity.y)
        print("Acceleration of ", PlanetList[i].name, PlanetList[i].acceleration.x, PlanetList[i].acceleration.y)
        PlanetList[i].Tick(PlanetList)
        turtle.penup()
        turtle.goto(PlanetList[i].position.x, PlanetList[i].position.y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(PlanetList[i].radius)
        turtle.end_fill()
        i = i + 1

    turtle.update()