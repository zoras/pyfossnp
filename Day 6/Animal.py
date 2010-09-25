class Animal:
    leg = ''
    type = ''
    def __init__(self, type = "Unknown"):
        self.type = type
    
    def setLeg(self,l):
        self.leg = l
    
    def getLeg(self):
        return self.leg
    
    def getType(self):
        return self.type
    
    def displayType(self):
        print self.type

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self,"Dog")
        
class Parrot(Animal):
    def __init__(self):
        Animal.__init__(self,"Parrot")
    def __str__(self):
        return self.getType()