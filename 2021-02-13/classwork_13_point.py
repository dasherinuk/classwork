class Point :
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def mul(self, m):
        new_x= self.__x * m
        new_y= self.__y * m
        return Point(new_x, new_y)
    
    def left(self,left1):
        left_x = self.__x -left1
        return Point(left_x,self.__y)

    def right(self,right1):
        right_x = self.__x + right1
        return Point(right_x,self.__y)

    def up(self,up1):
        up_y=self.__y +up1
        return Point(self.__x,up_y)
    
    def down(self,down1):
        down_y=self.__y -down1
        return Point(self.__x,down_y)

    def get_distance_X(self, point2):
        #abs(6 - 4) = 2
        #abs(4 - 6) = 2
        distance = self.__x - point2.__x
        
        return abs(distance)
    
    def get_distance_y(self,point2):
        distance = self.__y -point2.__y
        return abs(distance)

    def add(self,point2):
        total_X = self.__x + point2.__x
        total_Y = self.__y + point2.__y
        return (total_X,total_Y)
        
    def __str__(self):
        return f"({self.__x}, {self.__y})"

p1=Point(12,15)
p2=Point(19,7)

print(p2.left(2)) #left
print(p1.right(3)) #right
print(p2.up(5)) #up
print(p1.down(4)) #down

print(p1.get_distance_X(p2)) #x
print(p1.get_distance_y(p2)) #y

print(p1.add(p2))



print(p1)
print(p2)
print(p1.mul(10).mul(10))
