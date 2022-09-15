# 5. Write a python script to calculate the square of a number. Number is entered by the user.

numToBeSqr= int(input("Enter any number: "))

# using 
# 1. numToBeSqr**2 directly 
# 2. pow() method

def SQR(numToBeSqr):
    return numToBeSqr**2;

print(f'The square of number {numToBeSqr} is: {SQR(numToBeSqr)}')
    