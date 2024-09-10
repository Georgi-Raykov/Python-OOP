from Zoo.bear import Bear
from Zoo.lizard import Lizard
from Zoo.mammal import Mammal

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
bear = Bear('Balu')
print(bear.name)
print(bear.__class__.__bases__[0].__name__)