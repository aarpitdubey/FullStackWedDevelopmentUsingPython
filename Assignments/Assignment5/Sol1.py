# 1. Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)

user_input = int(input("Enter any number: "))

user_ip = user_input // 10

print(f'After removing the last digit of {user_input} is {user_ip}')