class Cat:
    #"constructor"
    #init ~ inicialisation
    #self - pointer on this object
    def __init__(self,name):
        self.name=name

    def mau(self):
        print(self.name, "Mau")

    def lick(self,cat):
        print(self.name, "Lick",cat.name)


    def eat(self):
        print(self.name, "Eat")

    

    def multy_mau(self, count):
        for i in range(count):
            self.mau()

    def mega_mau(self, count):
        self.mau()
        for i in range(count-1):
            print("Mau")
            
    def walk(self):
        print(self.name, "Walk")

    def kus(self, cat):
        print(self.name, " kus ", cat.name)
        #print(cat.name, " kus ", self.name)




c1 = Cat("Milka")
c2 = Cat("Eva")

c1.multy_mau(4)
c2.walk()
c2.mega_mau(5)
c1.eat()
c1.kus(c2)
c1.lick(c2)
