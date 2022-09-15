# 7. Write a python script to calculate average of three numbers, entered by the user

num1 = float(input("Enter  number 1: "))
num2 = float(input("Enter  number 2: "))
num3 = float(input("Enter  number 3: "))

def AvgOfThreeNum(n1, n2, n3):
    return (n1 + n2 + n3)/3

print(f'The Average of above three entered numbers {num1}, {num2}, and {num3} is: {AvgOfThreeNum(num1, num2, num3)}.')

