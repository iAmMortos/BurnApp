import ui

class TouchLayer (ui.View):
	
	def __init__(self):
		self.down_action = None
		self.up_action = None
	
	def touch_began(self, location):
		if self.down_action:
			self.down_action(location)
			
	def touch_ended(self, location):
		if self.up_action:
			self.up_action(location)
