class Human:
    def __init__(self,name):
        self.__name=name
        self.__dog=None

    def buy_dog(self,dog):
        if type (dog)==Dog:
            self.__dog=dog

    def stroke_dog(self):
        if self.__dog != None :
            self.__dog.stroke()

class Dog:
    def __init__(self,name):
        self.__name=name
        self.__happiness=50

    def stroke(self):
        self.__happiness=self.__happiness*2

    def __str__(self):
        return f"Dog: name={self.__name} happiness={self.__happiness}"

human = Human("Person")
dog = Dog("Belka")
human.buy_dog(dog)
print(dog)
human.stroke_dog()
print(dog)
human.stroke_dog()
print(dog)


        
