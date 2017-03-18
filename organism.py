#!/usr/bin/python3

class Organism(object):
	def __init__(self, size = 1):	
		self.size = size

	def update(self, world):
		raise NotImplementedError


class Animal(Organism):
	def __init__(self, speed = 5, sight = 100, food = 10, life = 10):
		super(Animal,self).__init__()
		self.type = "animal"
		self.speed = speed
		self.sight = sight
		self.food = food
		self.life = life

	def eatPlant(self, target):
		if target.size > 0:
			target.size -= 3
			self.food += 2

	def update(self, world):
		visible = world.getVisible(self)
		if len(visible) > 0:
			visible.sort(key = lambda x: world.getDistanceOrganisms(self, x), reverse = False)
			targetOrganism = visible[0]
			if targetOrganism.type == "plant":
				if world.getDistanceOrganisms(self, targetOrganism) < 0.5:
					self.eatPlant(targetOrganism)
				else:
					world.moveTowardsOrganism(self, targetOrganism, self.speed)
			elif targetOrganism.type == "animal":
				world.moveTowardsOrganism(self, targetOrganism, -self.speed)
		else:
			world.moveRandom(self, self.speed)

		# self.food -= 1
		if self.food < 1:
			self.life -= 1

		if self.food > 10:
			if self.life < 20:
				self.life += 1

		self.size = self.food

		if self.life < 1:
			world.killtargetOrganism(self)




class Plant(Organism):
	def __init__(self, size = 1):
		super(Plant,self).__init__()
		self.type = "plant"
		self.size = 1
				

	def update(self, world):
		if self.size < 20:
			self.size = self.size + 1

		if self.size < 2:
			world.killOrganism(self)



		
		

