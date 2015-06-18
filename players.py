class player(object):
	def __init__(self):
		self.location = [0,0]

	def move(self,direction):
		if direction == 'north':
			self.location = [self.location[0],self.location[1]+1]
		if direction == 'south':
			self.location = [self.location[0],self.location[1]-1]
		if direction == 'east':
			self.location = [self.location[0]+1,self.location[1]]
		if direction == 'west':
			self.location = [self.location[0]-1,self.location[1]]
		else:
			print 'Not a valid direction.'

	def warp(self,place):
		self.location = place

	def get_room(self,coord_dict):
		try:
			return coord_dict[str(self.location)]
		except:
			print 'Not a valid room'

	def gaze(self,direction): #Look in a particular direction to see what's there
		pass


