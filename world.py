#!/usr/bin/python3

import worldmap
import math
import random

class World(object):
	def __init__(self):
		self.map = worldmap.Worldmap()

	def addOrganism(self, organism, location = (-1,-1)):
		self.map.addOrganism(organism, location)

	def getVisible(self, organism):
		location = self.map.getOrganismLocation(organism)
		visible = []
		sightRange = int(organism.sight/2)
		print(location)
		for i in range(location[0]-sightRange, location[0]+sightRange):
			for j in range(location[1]-sightRange, location[1]+sightRange):
				contents = self.map.getLocationContents((i,j))
				if contents != None and contents != organism:
					visible.append(contents)
		return(visible)


	def moveTowardsOrganism(self, movingOrganism, dstOrganism, speed):
		srcLoc = self.map.getOrganismLocation(movingOrganism)
		dstLoc = self.map.getOrganismLocation(dstOrganism)
		D0 = dstLoc[0] - srcLoc[0]
		D1 = dstLoc[1] - srcLoc[1] 
		self.map.moveOrganism(movingOrganism, (D0,D1), speed)

	def moveRandom(self, moveOrganism, speed):
		D0 = random.randrange(90)
		D1 = random.randrange(90)
		self.map.moveOrganism(movingOrganism, (D0,D1), speed)


	def getDistBetweenOrganisms(self, organismA, organismB):
		srcLoc = self.map.getOrganismLocation(organismA)
		dstLoc = self.map.getOrganismLocation(organismB)
		D0 = dstLoc[0] - srcLoc[0]
		D1 = dstLoc[1] - srcLoc[1]
		# print(D0,D1)
		L = math.sqrt(pow(D0,2)+pow(D1,2))
		return(L)


	def killOrganism(self, organism):
		self.map.removeOrganism(organism)

	def update(self):
		organisms = list(self.map.getOrganisms())
		for organism in organisms:
			organism.update(self)
