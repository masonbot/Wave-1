Cash = int(input("Insert amount of cash in cents:"))
print(Cash//200, "Toonies")
Cash= Cash%200
print(Cash//100, "loonies")
Cash= Cash%100
print(Cash//25, "quarters")
Cash = Cash%25
print(Cash//10, "dimes")
Cash = Cash%10
print(Cash//5, "nickles")
Cash = Cash%5
print(Cash//1, "pennies")
Cash = Cash%1
