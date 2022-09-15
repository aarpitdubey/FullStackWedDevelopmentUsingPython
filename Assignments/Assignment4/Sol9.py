# 9. Write a python script to calculate the volume of a cuboid.

length = float(input("Enter the length of cuboid: "))
width  = float(input("Enter the width of cuboid:  "))
height = float(input("Enter the height of cuboid:  "))  

def VolOfCuboid(l, w, h):
    v = w*h*l
    return v

print(f'The volume of cuboid whose length is {length}, width {width} and , height {height} is {VolOfCuboid(length, width, height)}')