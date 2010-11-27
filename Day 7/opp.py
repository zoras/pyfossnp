class Bike:
    def __init__(self, model = "Unknown"):
        self.model = model
        print(model,"initialized")
    
    def showmodel(self):
        print(self.model)

b1 = Bike("Honda CBR")
b2 = Bike("Pulsar")

#b1.showmodel()
#b2.showmodel()

for b in [b1,b2]:
    print b.showmodel()