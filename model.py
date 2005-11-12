class NoMorePages(Exception):
	pass


class pagesContainer:
	pages = None
	queued = None
	newPageListeners = None


	def __init__(self):
		self.pages = []
		self.queued = []
		self.newPageListeners = []


	def add(self, page):
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



class _Project:
	settings = {
		'remoteDir': None,
		'localDir': None,
		'regExp': None,
	}
	pagesContainer = None


	def __init__(self):
		self.settings['firstUrl'] = 'http://localhost/common/sd.php'
		self.settings['localDir'] = '/usr/!'
		self.settings['regExp'] = '^.*$'
		self.pagesContainer = pagesContainer()


	def addUrl(self, url):
		page = Page(url, self.settings)
		self.pagesContainer.add(page)


	def storeNextPage(self):
		page = self.pagesContainer.popQueued()
		page.fetchContents()
		page.saveContents()



class Page:
	status = None
	url = None
	projectSettings = None

	path = None
	contents = None

	savingListeners = None


	def __init__(self, url, projectSettings):
		self.status = 'queued'
		self.projectSettings = projectSettings
		self.url = url
		self.path = projectSettings['localDir'] + url[len(projectSettings['remoteDir']):]
		self.savingListeners = []


	def fetchContents(self):
		import urllib
		self.contents = urllib.urlopen(self.url).read()


	def saveContents(self):
		dstFile = file(self.path, 'wb')
		dstFile.write(self.contents)
		dstFile.close()

		self.status = 'saved'

		self.notifySavingListeners()


	def addSavingListener(self, savingListener):
		self.savingListeners.append(savingListener)


	def notifySavingListeners(self):
		for savingListener in self.savingListeners:
			savingListener(self)


Project = _Project()
