class room(object):
	def __init__(self,location_title,someplace):
		self.coords = someplace
		self.title = location_title

	def set_stage(self):
		print '-----------------------------\n'+self.title+':'+'\n\n'+self.message+'\n'