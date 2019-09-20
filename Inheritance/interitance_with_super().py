class Animal:
	def __init__(self, animalName):
		print(animalName, 'is an animal')

class Mammal(Animal):
	def __init__(self, mammalName):
		print(mammalName, 'is a warm-blooded animal')
		super().__init__(mammalName)

class NonWingedMammal(Mammal):
	def __init__(self, NonWingedMammal):
		print(NonWingedMammal, 'can not fly')
		super().__init__(NonWingedMammal)

class NonMarineMammal(Mammal):
	def __init__(self, NonMarianeMammal):
		print(NonMarianeMammal, 'can not swim')
		super().__init__(NonMarianeMammal)

class Dog(NonMarineMammal, NonWingedMammal):
	def __init__(self):
		print('Dog has 4 legs')
		super().__init__('Dog')

d = Dog()
print('')
bat = NonMarineMammal('Bat')