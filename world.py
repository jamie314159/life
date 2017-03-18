#!/usr/bin/python3

import math
import random

class World(object):
	def __init__(self):
		self.map = {0:{0:[]}}
		self.locationList = {}

	def getMapContents(self, location):
		x,y = location
		if x in self.map:
			if y in self.map[x]:
				return(self.map[x][y])
		return([])

	def getDistanceLocations(self, locationA, locationB):
		x0,y0 = locationA
		x1,y1 = locationB
		return(math.sqrt(pow(abs(x1-x0),2)+pow(abs(x1-x0),2)))

	def getDistanceOrganisms(self, organismA, organismB):
		x0,y0 = self.getLocation(organismA)
		x1,y1 = self.getLocation(organismB)
		return(math.sqrt(pow(abs(x1-x0),2)+pow(abs(x1-x0),2)))


	def getLocation(self,organism):
		if organism in self.locationList.keys():
			return(self.locationList[organism])

	def addOrganism(self, organism, location = (0.0,0.0)):
		x,y = location
		xCell = int(x)
		yCell = int(y)

		if xCell not in self.map.keys():
			self.map[xCell] = {}

		if yCell not in self.map[xCell].keys():
			self.map[xCell][yCell] = []

		self.map[xCell][yCell].append(organism)
		self.locationList[organism] = location

	def removeOrganism(self, organism):
		x,y = self.getLocation(organism)
		xCell = int(x)
		yCell = int(y)

		# print(self.map)
		# print(self.map[xCell])
		# print(self.map[xCell][yCell])


		self.map[xCell][yCell].remove(organism)

		# if len(self.map[xCell][yCell]) == 0:
		# 	del self.map[xCell][yCell]

		# if len(self.map[xCell].keys()) == 0:
		# 	del self.map[xCell]
		del self.locationList[organism]

		


	def getVisible(self, organism):
		x,y = location = self.locationList[organism]
		x,y = int(x),int(y)
		r = organism.sight
		visible = []

		for i in range(x-r, x+r):
			for j in range(y-r, y+r):
				for seenOrganism in self.getMapContents((i,j)):
					if seenOrganism != organism and self.getDistanceOrganisms(organism, seenOrganism) < r:
						visible.append(seenOrganism)
		

		return(visible)

	def moveOrganism(self, organism, location):
		self.removeOrganism(organism)
		self.addOrganism(organism, location)

	def moveTowardsOrganism(self, agentOrganism, dstOrganism, speed):
		self.moveTowardsLocation(agentOrganism, self.getLocation(dstOrganism), speed)

	def moveTowardsLocation(self, organism, destination, speed):
		x0,y0 = self.getLocation(organism)
		x1,y1 = destination

		if x0 != x1 and y0 != y1:

			Dx = x1-x0
			Dy = y1-y0

			Dv = self.getDistanceLocations((x0,y0), destination)
			s  = organism.speed

			if Dv > s:
				dx = s * Dx / Dv
				dy = s * Dy / Dv
			else:
				dx = Dx
				dy = Dy
			
			self.moveOrganism(organism, (x0+dx, y0+dy))

	def moveRandom(self, agentOrganism, speed):
		D0 = random.randrange(90)
		D1 = random.randrange(90)
		self.moveOrganism(agentOrganism, (D0,D1))


	def killOrganism(self, organism):
		self.removeOrganism(organism)

	def update(self):
		organisms = list(self.locationList.keys())
		for organism in organisms:
			organism.update(self)
