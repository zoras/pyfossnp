import first_mod

first_mod.myprint("test")

class MyFirstClass:
    """This my 1st class"""
    def __init__(self):
        self.data = [1,2,3,4,5]
        
    def f(self):
        #return "hello frens"
        return self.data
        
mc = MyFirstClass()
print mc.f()
dir(mc)

print mc.__doc__
