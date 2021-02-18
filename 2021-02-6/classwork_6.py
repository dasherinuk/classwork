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

    def convert_time24(self):
        h = self.h
        if not self.beffor:
            h+=12
        return Time24(h, self.m)
                
    def __int__(self):
        return self.m + (self.h + 0 if self.beffor else 12)*60
    

    def __str__(self):
        return f"{self.h}:{self.m} {'AM' if self.beffor else 'PM'}"

class Time24:
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

    def convert_time12(self):
        h = self.h
        beffor = True
        if  h >= 12: 
            h-=12
            beffor = False
        return Time(h, self.m, beffor)

    def add_time(self, time2):
        sum_minutes = self.m + time2.m
        sum_hours = self.h + time2.h + sum_minutes//60
        sum_minutes = sum_minutes % 60
        sum_hours = sum_hours % 24
        return Time24(sum_hours, sum_minutes)

    
                
    def __int__(self):
        return self.m + (self.h )*60
    

    def __str__(self):
        return f"{self.h}:{self.m}"


t1 = Time(10,30,True)
t2 = t1.convert_time24()
print(t1)
print(t2)

t3 = Time(3,00,False)
t4 = t3.convert_time24()
print(t3)
print(t4)

t5=Time24(11,20)
t6= t5.convert_time12()
print(t5)
print(t6)

t7 = Time24(15,55)
t8 = t7.convert_time12()
print(t7)
print(t8)


print(t7.add_time(t5))

