class Bike:
    def __init__(self, model = "Unknown"):
        self.model = model
        print(model,"initialized")
    
    def showmodel(self):
        print(self.model)