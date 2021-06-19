bedtime,alarm = [int(item) for item in input().split()]
if bedtime<alarm:
    print(alarm-bedtime,"hours of sleep")
else:
    print(12-bedtime+alarm,"hours of sleep")
