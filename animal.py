#!/usr/bin/python3

# import organism

class Animal(organism.Organism)
	def __init__(self, speed = 10, sight = 10):
		super(Animal,self).__init__()
		self.type = "Animal"
		self.speed = speed
		self.sight = sight

	def update(self, world):
		print("test")
		canSee = world.getVisible(self, self.sight)
		for organism in canSee:
			print(self, organism)


		