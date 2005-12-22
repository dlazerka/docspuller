import Listened


class NoMorePages(Exception):
	pass


class PagesContainer:
	pages = None
	queued = None


	def __init__(self):
		self.pages = []
		self.queued = []
		self.urls = {}


	def add(self, page):
		self.urls[page.url] = True
		self.pages.append(page)
		page.id = self.pages.index(page)

		if page.status == 'queued':
			self.queued.append(page)

		self.notifyNewPageListeners(page)


	def popQueued(self):
		try:
			return self.queued.pop(0)
		except IndexError:
			raise NoMorePages()


	def containsUrl(self, url):
		return self.urls.has_key(url)


	addNewPageListener = Listened.getAddListenerMethod('newPage')
	notifyNewPageListeners = Listened.getNotifyListenersMethod('newPage')
