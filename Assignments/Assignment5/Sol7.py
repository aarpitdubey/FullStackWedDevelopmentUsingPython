# 7. Write a python script which takes a three digit number from the user and displays
# only its last digit.

n = input("\nEnter any three digit number: ")

if len(n) == 3:
    last_digit = int(n[2]);
    print(f'\nThe last digit of the three digit number {n} is {last_digit}.\n')
else:
    print("\nYou have entered Wrong digit value. Please re-check the number again. Thank you\n")
    