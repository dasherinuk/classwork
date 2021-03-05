class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

    def inside(self,x,y):
        return x<=self.width and y<=self.height

    def compare_size(self,x,y,rect2):
        return self.inside(x,y) and  self.inside(x+rect2.width,y) and  self.inside(x,y+rect2.height) and  self.inside(x+rect2.width,y+rect2.height)

if __name__=="__main__":
    rectangle = Rectangle(20,10)
    print(rectangle.inside(5,5))
    print(rectangle.inside(10,5))
    print(rectangle.inside(5,16))
    print(rectangle.inside(5,30))

    rectangle2 = Rectangle(5,5)

    print(rectangle.compare_size(2,2,rectangle2))
    print(rectangle.compare_size(7,2,rectangle2))
    print(rectangle.compare_size(3,17,rectangle2))
# rect 1
# 0, 0| width, height
# rect 2
# x, y| width, height
# надо проверить что все четыре вершины второго прямоугольника находяться
# находяться в нутри первого прямоугольника
# при вызове вункции нам срауз известно, что x,y это верхняя левая вершина
#второгоо прямоугольника
