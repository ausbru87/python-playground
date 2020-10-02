class Point():
	"""handles the creating and manipulating of x,y coordinates"""
	def __init__(self, initx=0, inity=0):
		self.x = initx
		self.y = inity
	
	def getX(self):
		return self.x
	
	def getY(self):
		return self.y
	
	def distanceFromOrigin(self):
		return ((self.x ** 2) + (self.y ** 2)) ** 0.5
		# this is the pythagorean thereom
	
	


p1 = Point(5)

print(p1.getY())
