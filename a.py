from model.Listened import *

class Foo1:
	propertyListeners = set()
	def addPropertyListener(self, listener):
		self.propertyListeners.add(listener)
	def notifyPropertyListeners(self, *pargs, **kargs):
		for listener in self.propertyListeners:
			listener(*pargs, **kargs)

			
class Foo2:
	addPropertyListener = getAddListenerMethod('property')
	notifyPropertyListeners = getNotifyListenersMethod('property')

f = Foo2()

def k():
	pass
f.addPropertyListener(k)
print f.addPropertyListener.im_class