class Salad:
    def __init__(self,name):
        self.__name=name
        self.__lettuce=None
        self.__carrot=None
        self.__mass=None

    def add_carrot(self,carrot):
        if type (carrot)==Carrot:
            self.__carrot=carrot

    def add_lettuce(self,lettuce):
        if type (lettuce)==Lettuce:
            self.__lettuce=lettuce

    
        

    def __str__(self):
        return f"Salad: name={self.__name} "


class Lettuce:
    def __init__(self,name):
        self.__name=name
        self.__mass=25
        self.__size=10

    def __str__(self):
        return "Lettuce: "+ self.__name

    def __str__(self):
        return f"Lettuce: name={self.__name} "

    #def mass_lettuce(self):
        #mass_lettuce = 1
        

class Carrot:
    def __init__(self,name):
        self.__name=name
        self.__mass=30
        self.__size=12
        

    def __str__(self):
        return "Carrot: "+ self.__name
    def __str__(self):
        return f"Carrot: name={self.__name} "


    #def mass_carrot(self):
        #mass_carrot = 1
salad=Salad("carrot and lettuce")
carrot=Carrot("carrot")
lettuce=Lettuce("lettuce")
salad.add_lettuce
salad.add_carrot
print(salad)
carrot.self.__mass
#mass=carrot.self.__mass + lettuce.self.__mass





