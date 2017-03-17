#!/usr/bin/python3


class Map(object):
	def __init__(self):
		self.byName = {}
		self.byLocation = {}

	def addOrganism(self, organism, location):
		self.byName[organism] = location
		self.byLocation[location[0]][location[1]] = organism
		
