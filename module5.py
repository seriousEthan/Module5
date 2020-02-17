# Ethan Martin
# Module 5

import math


def areaCircle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    return (print("The area of the circle is " + str(round(area, 2)) + " units rounded to 2 decimal points."))


areaCircle()


def brag(name, adj):
    return name[:6] + adj + name[5:]
print()

print(brag("Ethan Martin", "BadAss"))
print(brag("Ethan Martin", "SmartAss"))
print(brag("Ethan Martin", "DumbAss"))