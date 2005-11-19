class NoMorePages(Exception):
	pass


class PagesContainer:
	pages = None
	queued = None
	newPageListeners = None


	def __init__(self):
		self.pages = []
		self.queued = []
		self.newPageListeners = []


	def add(self, page):
		if len(self.pages) > 5:
			return False;
			
		self.pages.append(page)
		
		if page.status == 'queued':
			self.queued.append(page)

		self.notifyNewPageListeners(page)


	def popQueued(self):
		try:
			return self.queued.pop(0)
		except IndexError:
			raise NoMorePages()


	def addNewPageListener(self, newPageListener):
		self.newPageListeners.append(newPageListener);


	def notifyNewPageListeners(self, page):
		for newPageListener in self.newPageListeners:
			newPageListener(page)
