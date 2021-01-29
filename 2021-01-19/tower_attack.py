class Tower:
    def __init__(self,damage, hp):
        self.__damage=damage
        self.__hp = hp
        self.__target = None

    def setTarget(self, unit):
        if type(unit) == Unit or type(unit) == Health:
            self.__target = unit

    def isAlive(self):
        return self.__hp >0

    def give_damage(self,dmg):
        if dmg > 0:
            self.__hp -=dmg
    

    def give_health(self, hp):
        if hp>0:
            self.__hp += hp

    def attack(self):
        if self.__target and self.__target.isAlive():
            self.__target.give_damage(self.__damage)
            return True
        return False
    
    def __str__(self):
        return f"Tower: dmg={ self.__damage} hp={self.__hp }"
    

class Health:
    def __init__ (self, hp_revive, hp):
        self.__hp_revive = hp_revive
        self.__hp = hp
        self.__target= None   ###

    def setTarget(self, unit):
        if type(unit) == Unit or type(unit) == Health:
            self.__target = unit

    def add_hp(self):
        if self.__target and self.__target.isAlive():
            self.__target.give_health(self.__hp_revive)
            return True
        return False

    def isAlive(self):
        return self.__hp>0

    def give_health(self, hp):
        if hp>0:
            self.__hp += hp

    def give_damage(self, dmg):
        if dmg > 0:
            self.__hp -= dmg
    #вызываеться тогда когда необходимо преобразовать объект данного класса в строку
    def __str__(self):
        return f"Health: hp_revive={ self.__hp_revive} hp={self.__hp }"


class Catapult:
    def __init__ (self,name,damage, hp):
        self.__damage=damage
        self.__name=name
        self.__hp=hp
        self.__target = None

    def setTarget(self, tower):
        if type(tower) == Tower:
            self.__target = tower

    def attack(self):
        if self.__target and self.__target.isAlive():
            self.__target.give_damage(self.__damage)
            return True
        return False
        
    
    
class Unit:
    def __init__(self, name, damage, hp):
        self.__name = name
        self.__damage = damage
        self.__hp = hp
        self.__target = None

    def isAlive(self):
        return self.__hp>0

    def attack(self):
        if self.__target and self.__target.isAlive():
            self.__target.give_damage(self.__damage)
            return True
        return False

    def setTarget(self, unit):
        if type(unit) == Unit or type(unit)== Health:
            self.__target = unit

    def give_health(self, hp):
        if hp>0:
            self.__hp += hp

    def give_damage(self, dmg):
        if dmg > 0:
            self.__hp -= dmg

    def __str__(self):
        return f"Unit: {{name={self.__name} dmg={self.__damage}, hp={self.__hp}}}" #formated string (fstring)


unit = Unit("Maximilian", 10,100)
unit2 = Unit("Gregor", 20,200)
##print(unit)
tower = Tower(30, 1000)
health = Health(20,10)
catapult= Catapult("cat",100, 200)
#
catapult.setTarget(tower)
while catapult.attack():
    print(tower)
    
##tower.setTarget(unit)
##health.setTarget(unit)
##
##unit.setTarget(unit2)
##unit2.setTarget(unit)
##
##unit.setTarget(health)
##while unit.attack():
##    print(health)

##while unit.attack() and  unit2.attack() and health.add_hp():
##    print(unit, unit2)


##while tower.attack() and  health.add_hp():
##    print(unit)
##print(unit)

##print(tower)
##
##print(tower.attack())
##
##
##
##
##print(tower.attack())
##print(unit)
##print(unit2)
##
##tower.setTarget(unit)
##tower2 = Tower(40)
##Health = unit(10)
##tower3 = Tower(50)
##tower2.__damage=0
##tower2.setTarget(unit2)
##tower3.setTarget(unit2)
##
##for i in range(1,4):#1 2 3 
##    tower2.attack()
##
##tower3.attack()
##unit2.__hp=250
##print(unit2)
