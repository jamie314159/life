#!/usr/bin/python3


import world
import organism
import lifeDisplay

import random


def main():
	# init display
	myWindow = lifeDisplay.Window()

	# init world
	myWorld = world.World()
	# myWorld.addOrganism(organism.Animal(), (20,20))
	myWorld.addOrganism(organism.Animal(), (50,50))

	for i in range(2):
		myWorld.addOrganism(organism.Plant(), (random.randrange(100),random.randrange(100)))


	myWindow.world = myWorld
	myWindow.update()

	def update():
		myWorld.update()
		myWindow.update()
		myWindow.root.after(500,update)



	myWindow.root.after(0,update)
	myWindow.root.mainloop()	


if __name__ == '__main__':
	main()

