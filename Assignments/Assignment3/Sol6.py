num = int(input("Enter any number: "))
# print(hex(num).split('0x')[1].upper())

print(hex(num).replace('0x', '').upper())
