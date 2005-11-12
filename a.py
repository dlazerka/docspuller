class O:
	l = []

	def notify(self):
		pass

	def add(self, l):
		self.l.append(l)


class A(object, O, O):
	pass