totalseconds = float(input("Number of seconds: "))

day = totalseconds // (24 * 3600)
totalseconds = totalseconds % (24 * 3600)
hour = totalseconds // 3600
totalseconds %= 3600
minute = totalseconds // 60
totalseconds %= 60
second = totalseconds
print("%d:%d:%d:%d" % (day, hour, minute, second))