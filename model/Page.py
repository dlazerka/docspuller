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


	def __init__(self, url, settings):
		self.__status = 'queued'
		self.settings = settings
		self.url = url
		self.path = settings['localDir'] + url[len(settings['remoteDir']):]
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
		#print 'Page::fetchContents::self.url=%s' % self.url;
		import urllib
		urlOpener = urllib.URLopener()
		try:
			resource = urlOpener.open(self.url)
		except IOError:
			self.status = 'failed'
			return False;
		else:
			self.contents = resource.read()
			self.status = 'fetched'
			return True
		#print 'Page::fetchContents::len=%d' % len(self.contents);


	def saveContents(self):
		#print 'Page::saveContents::%s' % self.path;

		dstFile = file(self.path, 'wb')
		dstFile.write(self.contents)
		dstFile.close()

		self.status = 'saved'


	def parse(self):
		import re
		links = re.findall('(?:href|rel|src)="([^"]+)"', self.contents)
		# http://localhost/common/sd.php
		# //localhost/common/sd.php
		# /common/sd.php
		# sd.php

		remoteDomain = re.match('http://([^/]+)', self.settings['remoteDir']).group(1)
		for link in links:
			groups = list(re.match('(http:)?(//[^/]+)?(/)?(.*)', link).groups())
			if not groups[0]:
				groups[0] = 'http:'
			if not groups[1]:
				groups[1] = '//' + remoteDomain
			if not groups[2]:
				groups[2] = '/'

			link = ''.join(groups)
			#if \
			#	link[0:len(self.settings['remoteDir'])] == self.settings['remoteDir']\
			#	and re.search(self.settings['regExp'], link)\
			#	and not
			#:
			#	self.links.append(link)

		return self.links
