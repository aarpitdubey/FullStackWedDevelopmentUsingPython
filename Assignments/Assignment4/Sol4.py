# 4. Write a python script which takes the radius from the user and display area of a circle.
import math
radius = float(input("Enter the radius: "))

def AreaOfCircle(radius):
    area = math.pi * (radius**2)
    return area

print(f'The Area of the Circle is : {AreaOfCircle(radius)}\nwhose radius is : {radius}')