oct_num = oct(25).replace('0o', '')
hex_num = hex(39).replace('0x', '')
bin_sum = int(oct_num) + int(hex_num)

print(f"We have 25 in octal number: {oct_num}, \nWe have 39 in Hexadecimal number: {hex_num} \n{oct_num} + {hex_num} = {bin_sum} \nIn Binary number format for {bin_sum} it is: {bin(bin_sum).replace('0b', '')}")