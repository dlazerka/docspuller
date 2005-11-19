class SDStatusError(Exception):
	pass



class SDStatus(object):
	""" Descriptor """


	value = 'inactive'
	possible = ('inactive', 'active')
	action = None


	def __init__(self, action = None):
		self.action = action


	def __get__(self, instance, owner):
		return self.value


	def __set__(self, instance, value):
		if self.value == value or value not in self.possible:
			raise SDStatusError, "Bad status '%s', possible: '%s'" % (value, self.possible)
		else:
			self.value = value
			if value == 'active':
				if callable(self.action):
					self.action(instance)
				else:
					raise SDStatusError, "Empty self.action"
