from Animal import *

Mark = Dog()
Mark.setLeg(4)

Tommy = Dog()
Tommy.setLeg(4)

Harry = Parrot()
Harry.setLeg(2)

Smith = Parrot()
Smith.setLeg(2)

#print Smith
#Harry.displayType()
print Harry.getLeg()

animals = [Mark, Smith, Harry, Tommy]

delect = lambda a: a.getType()

print animals, map(delect, animals)

typeDogs = lambda a: a.getType() == "Dog"
typeParrots = lambda a: a.getType() == "Parrot"

print filter(typeDogs, animals)
print filter(typeParrots, animals)