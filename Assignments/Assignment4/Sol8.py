# 8. Write a python script to calculate simple interest

P = float(input("Enter the Principal Amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the TimePeriod taken: "))

def SimpleInterest(P, R, T) :
    SI = (P*R*T)/100
    return SI

print(f'\nThe Simple Interest of entered Principla amt {P}, Rate of Interest {R}, and Time Period {T} is {SimpleInterest(P, R, T)}')
