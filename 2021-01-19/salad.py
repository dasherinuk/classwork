class Salad:
    def __init__(self,name):
        self.__name=name
        self.__lettuce=None
        self.__carrot=None

    def add_carrot(self,carrot):
        if type (carrot)==Carrot:
            self.__carrot=carrot

    def add_lettuce(self,lettuce):
        if type (lettuce)==Lettuce:
            self.__lettuce=lettuce

    def calc_mass(self):          
        return self.get_mass_lettuce() + self.get_mass_carrot()

    def get_mass_carrot(self):
        return self.__get_mass_ingridient(self.__carrot)

    def get_mass_lettuce(self):
        return self.__get_mass_ingridient(self.__lettuce)

    def __get_mass_ingridient(self, ingridient):
        if ingridient==None:
            return 0
        return ingridient.get_mass()
        
    def __str__(self):
        return f"Salad: name={self.__name} mass={self.calc_mass()}"


class Lettuce:
    def __init__(self,name):
        self.__name=name
        self.__mass=25
        self.__size=10

    def get_mass(self):
        return self.__mass

    def __str__(self):
        return f"Lettuce: name={self.__name} "


        
class Carrot:
    def __init__(self,name):
        self.__name=name
        self.__mass=30
        self.__size=12

    def get_mass(self):
        return self.__mass
        
    def __str__(self):
        return f"Carrot: name={self.__name} "



salad=Salad("carrot_and_lettuce")
carrot=Carrot("carrot")
lettuce=Lettuce("lettuce")
salad.add_lettuce(lettuce)
salad.add_carrot(carrot)
print(salad)






