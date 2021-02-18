class Racional:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator=denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def convert(self):
        return self.numerator/self.denominator

    def mul(self, other):
        numerator = self.numerator*other.numerator
        denominator = self.denominator*other.denominator
        return Racional(numerator,denominator)

    def add(self, other ):
        denominator_1 = self.denominator * other.denominator
        numerator_1 = self.numerator * other.denominator
        numerator_2 = other.numerator * self.denominator
        new_numerator= numerator_1 + numerator_2
        return Racional(new_numerator,denominator_1)
        
        

    def sub(self, other):
        denominator_1 = self.denominator * other.denominator
        numerator_1 = self.numerator * other.denominator
        numerator_2 = other.numerator * self.denominator
        new_numerator= numerator_1 - numerator_2
        return Racional(new_numerator,denominator_1)

    def div(self, other): 
        numerator_1=self.numerator * other.denominator
        denominator_1=self.denominator * other.numerator
        return Racional(numerator_1,denominator_1)

    

        
        

r= Racional(10,25)
r2 = Racional(25,40)
print(r)
#print(r.convert())
print(r.mul(r2))
print(r.add(r2))
print(r.sub(r2))
print(r.div(r2))
