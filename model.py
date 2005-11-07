class SiteDownloader(object):
	state = None
	currentProject = None


	@classmethod
	def getCurrentProject(cls):
		if cls.currentProject == None:
			cls.currentProject = Project()

		return cls.currentProject



class Project(object):
	firstUrl = None
	localPath = None
	regExp = None
	pagesCollection = None
	observers = None


	def __init__(self):
		firstUrl = 'http://localhost/common/sd.php'
		localPath = '/usr/!'
		regExp = '^.*$'
		self.pagesCollection = PagesCollection()
		observers = []


	def registerObserver(self, observer):
		self.observers = observer


	def notifyObservers(self):
		for observer in self.observers:
			observer()


	def addPage(self, page):
		self = Project
		self.pages.append(page)

		if page.status == 'queued':
			self.pagesQueued.append(page)


	def popQueuedPage(self):
		self = Project
		if len(self.queuedPages) > 0:
			return self.queuedPages.pop(0)
		else:
			return None



class PagesCollection(object):
	pages = None

	def __init__(self):
		pages = []



class Page:
	status = None
	url = None
	path = None
	contents = None

	def __init__(self, url):
		self.status = 'queued'
		self.url = url

	def getContents(self):
		import urllib
		self.contents = urllib.urlopen(self.url).read()

	def setPath(self, path):
		self.path = path

	def setStatus(self, status):
		self.status = status
