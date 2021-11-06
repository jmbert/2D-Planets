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

    def Scale(self, b) :
        return Vector(self.x * b, self.y * b)
    
    def Length(self) :
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def Normalize(self) :
        return self.Scale(1 / self.Length())

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
    
    def __sub__(self, b) :
        return Vector(self.x - b.x, self.y - b.y)


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
        attraction = G * self.mass * b.mass / pow((self.position - b.position).Length(), 2) / -self.mass

        print(self.name, " Distance to ", b.name, (self.position - b.position).Length())
        print(self.name, "Attraction to ", b.name, attraction)

        print("\n", "\n")

        return attraction

    def Tick(self, PlanetList) :
        i = 0
        while i < len(PlanetList) :
            if (PlanetList[i] != self) :
                self.acceleration = (self.position - PlanetList[i].position).Normalize() * math.floor(self.CalculateAttraction(PlanetList[i]))
            i = i + 1
        self.velocity = Vector(self.velocity.x + self.acceleration.x, self.velocity.y + self.acceleration.y)
        self.position = Vector(self.position.x + self.velocity.x, self.position.y + self.velocity.y)

        if self.position.x < -s.window_width() / 2 :
            self.position.x = -s.window_width() / 2
        elif self.position.x > s.window_width() / 2 :
            self.position.x = s.window_width() / 2
        if self.position.y < -s.window_height() / 2 :
            self.position.y = -s.window_height() / 2
        elif self.position.y > s.window_height() / 2 :
            self.position.y = s.window_height() / 2  

Earth = Planet("Earth", 10, 1000, Vector(10, 0), Vector(0, 0))
Moon = Planet("Moon", 7, 100, Vector(0, 0), Vector(0, 50))

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