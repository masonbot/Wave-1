import math

pi = math.pi 

Height = input("Height of cylinder in metres: ")
Radius = input("Radius of cylinder in metres: ")

r2 = float(Radius) * float(Radius)
area = float(pi) * (r2) * float(Height)

print(round(area,1))