#main.py
from race_car import RaceCar
from car import Car
from plane import Plane
from boat import Boat

race_car = RaceCar("McLaren F1", 370, 2, 950)
car = Car("Hatchback", 120, 5)
plane = Plane("Airbus A380", 1020, 79)
boat = Boat("Speedboat", 150, 12)

race_car.display_info()
car.display_info()
plane.display_info()
boat.display_info()

#Vehicle.py
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def display(self):
        print(f"Vehicle Name: {self.name}, Speed: {self.speed}")

#Car.py
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, speed, doors):
        super().__init__(name, speed)
        self.doors = doors

    def display(self):
        super().display() 
        print(f"Doors: {self.doors}")

#Boat.py
from vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, name, speed, length):
        super().__init__(name, speed)
        self.length = length

    def display(self):
        super().display() 
        print(f"Length: {self.length} meters")

#Plane.py
from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, name, speed, wingspan):
        super().__init__(name, speed)
        self.wingspan = wingspan

    def display(self):
        super().display() 
        print(f"Wingspan: {self.wingspan} meters")

#race_car.py
from car import Car

class RaceCar(Car):
    def __init__(self, name, speed, doors, horsepower):
        super().__init__(name, speed, doors)
        self.horsepower = horsepower

    def display(self):
        super().display() 
        print(f"Horsepower: {self.horsepower} hp")

