# 10. Write a python script to display the current date and time. First create variables to store date and time, then display date and time in proper format (like: 13-8-2022 and 9:00 PM)

import datetime
print("Solution 10:")
dt=datetime.datetime.now()
date=dt.strftime("%d-%m-%Y")
time=dt.strftime("%I:%M %p")
print(f"Date is {date} and Time is {time}")
print("*"*80)
print()