import ui
import os
import sound
from touch_layer import TouchLayer


class FireView (ui.View):
	
	def did_load(self):
		self.fire_wv = self['fire_wv']
		self.touch_layer = self['touch_layer']
		filename = os.path.abspath('html/fire.html')
		self.fire_wv.load_url(filename)
		self.background_color = '#000'
		self.airhorn_sound = sound.play_effect('rsc/airhorn.m4a')
		self.touch_layer.down_action = self.handle_touch
		
	def will_close(self):
		if self.airhorn_sound:
			self.airhorn_sound.stop()
		
	def handle_touch(self, event):
		if self.airhorn_sound:
			self.airhorn_sound.stop()
		self.airhorn_sound = sound.play_effect('rsc/airhorn_single.m4a')
	
	@staticmethod
	def load_view():
		return ui.load_view()
