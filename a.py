import model.Listened as Listened

class A:
	addPropertyListener = Listened.getAddListenerMethod('property')
	notifyPropertyListeners = Listened.getNotifyListenersMethod('property')
	
	def kuku(self, asd):
		pass
		

def asd(**args):
	print args

b = {'f': 'd'}
asd(**b)
	
