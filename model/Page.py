class Page(object):
	"""
	__status
	url
	settings
	path
	contents
	statusListeners
	links
	"""


	def __init__(self, url, settings, parent = None):
		self.__status = 'queued'
		self.settings = settings
		self.url = url
		self.relPath = url[len(settings['remoteDir']) + 1:]
		self.statusListeners = []
		self.links = []


	def getStatus(self):
		return self.__status


	def setStatus(self, value):
		self.__status = value
		self.notifyStatusListeners()


	status = property(getStatus, setStatus)


	def addStatusListener(self, statusListener):
		self.statusListeners.append(statusListener)


	def notifyStatusListeners(self):
		for statusListener in self.statusListeners:
			statusListener(self)


	def fetchContents(self):
		self.status = 'fetching...'
		try:
			import urllib
			resource = urllib.URLopener().open(self.url)
		except IOError:
			self.status = 'fetching failed'
			return False
		else:
			self.contents = resource.read()
			self.status = 'fetched'
			return True


	def saveContents(self):
		import os

		subdirs = self.relPath.split('/')[:-1]
		cur = self.settings['localDir']
		for subdir in subdirs:
			cur = cur + '/' + subdir
			if not os.path.exists(cur):
				os.mkdir(cur)

		path = '%s/%s' % (self.settings['localDir'], self.relPath)
		try:
			dstFile = file(path, 'wb')
		except IOError:
			self.status = 'saving failed'
			raise
		else:
			dstFile.write(self.contents)
			dstFile.close()
			self.status = 'saved'


	def parse(self):
		import re
		import urlparse

		for link in re.findall('(?:href|rel|src)="([^"]+?)"', self.contents):
			link = urlparse.urljoin(self.url, link)
			if link[0:len(self.settings['remoteDir'])] == self.settings['remoteDir']\
				and re.search(self.settings['regExp'], link)\
			:
				self.links.append(link)

		self.status = 'parsed'
