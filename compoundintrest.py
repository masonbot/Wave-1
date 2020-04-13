Money = input("Initial amount deposited:")

year1 = float(Money) * 1.04
year2 = float(year1) * 1.04
year3 = float(year2) * 1.04

print(round(year1,2))
print(round(year2,2))
print(round(year3,2))