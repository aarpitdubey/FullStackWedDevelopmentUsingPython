# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.

# import math

side1 = float(input("Enter side1 of triangle: "))
side2 = float(input("Enter side2 of triangle: "))
side3 = float(input("Enter side3 of triangle: "))


def areaOfTriangle(s1, s2, s3):
    sp = (s1 + s2 + s3)/2; # semi perimeter "sp"
    # area = math.sqrt(sp*(sp - s1)*(sp - s2)*(sp - s3))
    area = (sp*(sp - s1)*(sp - s2)*(sp - s3))**0.5
    return area


print(f'The Area of triangle whose sides are {side1}, {side2} and {side3} is: {areaOfTriangle(side1, side2, side3)}.')