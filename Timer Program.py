#Counter timer program

import time

timer = int(input("Enter a time: "))

for x in reversed(range(0, timer)):
    hours = x % 60
    minutes = int(x / 60) % 60
    seconds =  int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")