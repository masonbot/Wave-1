secondsday = 86400
secondshour = 3600
secondsminute = 60

day =int(input("Number of Days: "))
hour = int(input("Number of hours: "))
minute = int(input("Number of minutes: "))
second = int(input("Number of seconds: "))

totalseconds = day * secondsday
totalseconds = totalseconds + (hour * secondshour)
totalseconds = totalseconds + (minute * secondsminute)
totalseconds = totalseconds + second

print("Total seconds: ", totalseconds)