

class desc(object):
	def __get__(self, instance, owner):
		print self
		print instance
		print owner

	def __set__(self, instance, value):
		print 'setter!'
		if value.__class__ == desc:
			self = value

	def __delete__(self, instance):
		print instance

	def ku(self):
		return 10


class A(object):
	d = desc()

	def set(self, val):
		self.d = val


import inspect as i

a = A()
print id(a)
a.d = 'ku'
print a.d
print id(a)
