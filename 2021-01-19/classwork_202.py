class Time:
    def __init__(self, h, m, beffor):
        self.h = h
        self.m = m
        self.beffor = beffor

    def add_minutes(self,minutes):
        minutes_1 = self.m + minutes
        beffor_1 = self.beffor
        hours_1=self.h + minutes_1//60
        minutes_1 = minutes_1%60
            
        while hours_1>=12:
            hours_1= hours_1 - 12
            beffor_1 = not beffor_1
                
        return Time(hours_1, minutes_1, beffor_1)


    def add_hours(self,hours):
        hours_1 = self.h + hours
        beffor_1 = self.beffor

        while hours_1>=12:
            hours_1 = hours_1 - 12
            beffor_1 = not beffor_1
                
        return Time(hours_1, self.m, beffor_1)
                
    def __int__(self):
        return self.m + (self.h + 0 if self.beffor else 12)*60
    

    def __str__(self):
        return f"{self.h}:{self.m} {'AM' if self.beffor else 'PM'}"


t1 = Time(11,29, True)
t2 = Time(8, 35, False)

print(t1)
print(t2)

print(t1.add_minutes(50))
print(t1.add_minutes(1200))
print(t1.add_hours(5))
print(t1.add_hours(29))
print(int(t1))
##t_error = Time(28,35, False)
##print(t_error)
