#!/usr/bin/python3

from tkinter import *
from tkinter import ttk


def circleAt(location,size):
	x,y = location
	r = size//2
	return((x-r,y-r,x+r,y+r))

class Window():
	def __init__(self, size=1000):
		self.root = Tk()
		self.root.minsize(size, size)
		self.root.geometry(str(size)+'x' + str(size))
		self.canvas = Canvas(self.root, width=size, height=size, bg = "beige")
		self.canvas.place(relx=.01, rely=.01, anchor=NW)

		self.world = None

		
		# self.root.after(100, self.animate())
		# self.root.mainloop()
		






	def update(self):
		self.canvas.delete('all')
		if self.world != None:
			windowMap = self.world.locationList
			for organism in windowMap.keys():
				size = organism.size
				location = windowMap[organism]
				organismSizeShape = self.canvas.create_oval(circleAt(location,size))

				newSizeCoords = (location[0],location[1],location[0]+size,location[1]+size)

				if organism.type == "Animal":
					sight = organism.sight
					organismSightShape = self.canvas.create_oval(circleAt(location,sight))




				# i = location[0]
				# j = location[1]
				# self.canvas.create_oval(i*10+2, j*10+2, i*10+2+size, j*10+2+size)
				# self.canvas.create_oval(i*10-2, j*10-2, i*10+4+size, j*10+4+size)




			self.canvas.update()
		else:
			self.canvas.update()			
		# self.root.after(100, self.animate())






