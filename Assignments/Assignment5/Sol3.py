# 3. Write a python script to swap data of two variables

var1 = input("Enter value for Var1: ")
var2 = input("Enter value for Var2: ")
var3 = 0;

print(f'\nBefore swapping value are:\nvar1 : {var1} and, \nvar2 : {var2}')

#swap
var3 = var1;
var1 = var2;
var2 = var3;

print(f'\nAfter swapping value are:\nvar1 : {var1} and, \nvar2 : {var2}')
