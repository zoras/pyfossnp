## inhiritance

class Bike:
    def __init__(self, model = "Unknown"):
        self.model = model
        print(model,"initialized")
    
    def showmodel(self):
        print(self.model)


class Powerbike (Bike):
    def __init__(self,model,cc):
        Bike.__init__(self,model)
        self.cc = cc
    
    def showpower(self):
        print self.cc

p1 = Powerbike('Harnet',700)
p1 = showmodel()
p1 = showpower()