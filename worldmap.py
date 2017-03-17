#!/usr/bin/python3

import math

class Worldmap(object):
	def __init__(self):
		self.byName = {}
		self.byLocation = {}

	def addOrganism(self, organism, location):
		self.byName[organism] = location
		if location[0] not in self.byLocation:
			self.byLocation[location[0]] = {}
		self.byLocation[location[0]][location[1]] = organism

	def removeOrganism(self, organism):
		location = self.getOrganismLocation(organism)
		del self.byLocation[location[0]][location[1]]
		del self.byName[organism]

	def getOrganismLocation(self, organism):
		return(self.byName[organism])

	def getLocationContents(self, location):
		if location[0] in self.byLocation:
			if location[1] in self.byLocation[location[0]]:
				return(self.byLocation[location[0]][location[1]])
		return(None)

	def getLocationsByOrganism(self):
		return(self.byName)

	def moveOrganism(self, organism, move, speed):
		L = math.sqrt(pow(move[0],2)+pow(move[1],2))
		while speed >= L:
			speed = speed / 2
		print("speed",speed)
		d0 = move[0]/L*speed
		d1 = move[1]/L*speed
		d0 = (math.ceil(d0) if d0>0 else math.floor(d0))
		d1 = (math.ceil(d1) if d1>0 else math.floor(d1))
		
		s0,s1 = self.getOrganismLocation(organism)
		
		while self.getLocationContents((s0+d0,s1+d1)) != None:
			d0 = (d0 + 1 if d0>0 else d0-1)
			d1 = (d1 + 1 if d1>0 else d1-1)


		self.removeOrganism(organism)
		self.addOrganism(organism, (s0+d0,s1+d1))
		# if self.getLocationContents((s0+d0,s1+d1)) == None:
		# 	self.removeOrganism(organism)
		# 	self.addOrganism(organism, (s0+d0,s1+d1))
		



	def getOrganisms(self):
		return(self.byName.keys())
