# 6. Write a python script which takes a three digit number from the user and displays
# only its middle digit.

n = input("\nEnter any three digit number: ")
if len(n) == 3:
    middle_number=int(n[1])
    print(f'\nThe middle digit of the three digit number {n}, is {middle_number}.\n')
else:
    print(f'\nThe entered count of digits of the numbers exceeded three so, re-check the entered value.\n')

