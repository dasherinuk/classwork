class Cat:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "Cat: " + self.name
    
class Dog:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "Dog: "+ self.name

class Human:
    def __init__(self,name):
        self.name=name
        self.cats=[]
        self.dogs=[]

    def add_cat(self,cat):
        if type(cat)==Cat:
            self.cats.append(cat)
    
    def add_dog(self,dog):
        if type(dog)==Dog:
            self.dogs.append(dog)

    def __str__(self):
        result = self.name + "\n"
        for cat in self.cats:
            result +=" " + str(cat)
        result+="\n"
        for  dog in self.dogs:
            result +=" " + str(dog)
        return result

    def __eq__(self, human):
        return len(self.cats) + len(self.dogs) == len(human.cats) + len(human.dogs) 


    def __lt__(self, human):
        return len(self.cats) + len(self.dogs) < len(human.cats) + len(human.dogs) 


h1 = Human("Ivan")
h2 = Human("Petr")

print(h1)
print(h2)

h1.add_cat(Cat("Marusya"))
h1.add_dog(Dog("Tusik"))
h1.add_dog(Cat("Leon"))
h1.add_dog(1)
#h1.dogs.append(45)#error incapsuletion
h2.add_cat(Cat("Barsik"))
h2.add_cat(Cat("Belka"))
h2.add_cat(900)
#h2.cats.append(100)#error incapsuletion


print(h1)
print(h2)

print(h1==h2)

print(h1<h2)
print(h1>h2)
