#!/usr/bin/python3

class Organism(object):
	def __init__(self, size = 10):	
		self.size = size

	def update(self, world):
		raise NotImplementedError


class Animal(Organism):
	def __init__(self, speed = 5, sight = 20, food = 10, life = 10):
		super(Animal,self).__init__()
		self.type = "animal"
		self.speed = speed
		self.sight = sight
		self.food = food
		self.life = life

	def eatPlant(self, target):
		if target.size > 0:
			target.size -= self.size * 0.2
			self.food += self.size * 0.2

	def update(self, world):
		visible = world.getVisible(self)
		if len(visible) > 0:
			visible.sort(key = lambda x: world.getDistBetweenOrganisms(self, x), reverse = False)
			organism = visible[0]
			if organism.type == "plant":
				if world.getDistBetweenOrganisms(self, organism) < 2.5:
					self.eatPlant(organism)
				else:
					world.moveTowardsOrganism(self, organism, self.speed)
			elif organism.type == "animal":
				world.moveTowardsOrganism(self, organism, -self.speed)
		else:
			world.moveRandom(self, speed)

		self.food -= 1
		if self.food < 1:
			self.life -= 1

		if self.food > 10:
			if self.life < 20:
				self.life += 1

		self.size = self.food

		if self.life < 1:
			world.killOrganism(self)




class Plant(Organism):
	def __init__(self, size = 1):
		super(Plant,self).__init__()
		self.type = "plant"
		self.size = 1
				

	def update(self, world):
		if self.size < 20:
			self.size = self.size + 1

		if self.size < 1:
			world.killOrganism(self)



		
		

