def getAddListenerMethod(name):
	
	listenersListName = '__%sListeners' % name
	functionName = 'add%sListener' % name.capitalize()
	
	def f(self, listener):
		if not hasattr(self, listenersListName):
			setattr(self, listenersListName, [])
			
		listenersList = getattr(self, listenersListName)
		listenersList.append(listener)
	
	f.__name__ = functionName
	
	return f


def getNotifyListenersMethod(name):

	listenersListName = '__%sListeners' % name
	functionName = 'add%sListener' % name.capitalize()
	
	def tmp(self, *pargs, **kargs):
		if hasattr(self, listenersListName):
			for listener in getattr(self, listenersListName):
				listener(*pargs, **kargs)
		
	tmp.__name__ = functionName
	
	return tmp
