class Animal:
    leg = ''
    type = ''
    def __init__(self, type = "Unknown"):
        self.type = type
    
    def setLeg(self,l):
        self.leg = l
    
    def displayType(self):
        return self.type

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self,"Dog")
        
class Parrot(Animal):
    def __init__(self):
        Animal.__init__(self,"Parrot")