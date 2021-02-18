class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m
        
       

    def add_minutes(self,minutes):
        minutes_1 = self.m + minutes
        hours_1=self.h + minutes_1//60
        minutes_1 = minutes_1%60
        hours_1= hours_1 % 24
        return Time(hours_1, minutes_1)

    def add_hours(self,hours):
        hours_1 = self.h + hours
        hours_1 = hours_1 % 24

        return Time(hours_1 , self.m)

    def __float__(self):
        return self.h + self.m/60
                
    def __int__(self):
        return self.m + (self.h )*60
    

    def __str__(self):
        return f"{self.h}:{self.m}"


t1 = Time(11,29)
t2 = Time(20,35)

print(t1)
print(t2)

print(float(t1))
print(float(t2))

print(t1.add_minutes(10))
print(t1.add_minutes(50))  ##problem
print(t1.add_hours(29))

#t_error = Time(28,35, False)
#print(t_error)
