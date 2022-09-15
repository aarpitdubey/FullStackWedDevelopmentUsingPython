# 4. Write a python script to find x power y, where values of x and y are given by user
x =  int(input("Enter value of x: "))
y =  int(input("Enter value of y: "))
def power(x, y):
    return x**y;

print(f'Value of x is {x}.\nValue of y is {y}.\nx power y  is {power(x, y)}.')
