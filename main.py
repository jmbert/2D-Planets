import turtle
import time
import math

turtle.tracer(0, 0)
turtle.speed(0)

s = turtle.Screen()

DeltaTime = 1

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
        attraction = G * self.mass * b.mass / -pow((self.position - b.position).Length(), 2) / self.mass

        print(self.name, " Distance to ", b.name, (self.position - b.position).Length())
        print(self.name, "Attraction to ", b.name, attraction)

        return attraction

    def Tick(self, PlanetList) :
        i = 0
        while i < len(PlanetList) :
            if (PlanetList[i] != self) :
                self.acceleration = self.position - PlanetList[i].position.Normalize() * self.CalculateAttraction(PlanetList[i])
            i = i + 1
        self.velocity = self.velocity + self.acceleration * DeltaTime
        self.position = self.position + self.velocity * DeltaTime

        print("Position of ", self.name, self.position.x, self.position.y)
        print("Velocity of ", self.name, self.velocity.x, self.velocity.y)
        print("Acceleration of ", self.name, self.acceleration.x, self.acceleration.y)

        print("\n")

        if self.position.x < -s.window_width() / 2 :
            self.position.x = -s.window_width() / 2
        elif self.position.x > s.window_width() / 2 :
            self.position.x = s.window_width() / 2
        if self.position.y < -s.window_height() / 2 :
            self.position.y = -s.window_height() / 2
        elif self.position.y > s.window_height() / 2 :
            self.position.y = s.window_height() / 2  

Earth = Planet("Earth", 10, 1000, Vector(0, 0), Vector(0, 0))
Moon = Planet("Moon", 5, 10, Vector(0, 0), Vector(0, 100))

PlanetList = [Earth, Moon]

while True :
    time.sleep(DeltaTime)
    s.clearscreen()
    turtle.tracer(0, 0)
    turtle.speed(0)
    turtle.ht()
    i = 0
    while i < len(PlanetList) :
        
        PlanetList[i].Tick(PlanetList)
        turtle.penup()
        turtle.goto(round(PlanetList[i].position.x), round(PlanetList[i].position.y))
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(PlanetList[i].radius)
        turtle.end_fill()
        i = i + 1

    turtle.update()