# 10. Write a python script to calculate area of a rectangle

from turtle import width


length = float(input("Enter the length of rectangle:  "))
width  = float(input("Enter the width of  rectangle:  "))

def findAreaOfRect(length, width):
    area = length * width
    return area

print(f'\nThe Area of the rectangle whose length is {length} and width is {width} is: {findAreaOfRect(length, width)}.')

