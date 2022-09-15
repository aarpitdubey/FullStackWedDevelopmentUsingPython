# 2. Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)

# To get the last digit from a number we just divided it by 10 and reminder is the last digit


user_input = int(input("Enter any number:"))
rem = user_input%10;

print(f'The last digit of {user_input} is {rem}')

