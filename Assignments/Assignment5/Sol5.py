# 5. Write a python script which takes a three digit number from the user and displays
# only its first digit.

# 3 digit numbers means those in the row of 100's
# 100 (hundreds) * x + 10 (Tens) * y + c (One's)

n = int(input("Enter any number of three digits: "))
out = n//100
print(f"\nThe first digit of the three digit number {n} is {out}.\n")