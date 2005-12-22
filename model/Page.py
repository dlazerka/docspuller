import re

import Listened


class Page(object):
	def __init__(self, url, projectCfg, parent = None):
		self.url = url
		self.projectCfg = projectCfg
		self.parent = parent
		self.relPath = url[len(projectCfg.remoteDir) + 1:]
		self.links = []

		if re.search(self.projectCfg.regExp, url):
			self.__status = 'queued'
		else:
			self.__status = 'failed regexp'


	def getStatus(self):
		return self.__status


	def setStatus(self, value):
		self.__status = value
		self.notifyStatusListeners(self)


	status = property(getStatus, setStatus)


	addStatusListener = Listened.getAddListenerMethod('status')
	notifyStatusListeners = Listened.getNotifyListenersMethod('status')


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
		cur = self.projectCfg.localDir
		for subdir in subdirs:
			cur = cur + '/' + subdir
			if not os.path.exists(cur):
				os.mkdir(cur)

		path = '%s/%s' % (self.projectCfg.localDir, self.relPath)
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
			if link[0:len(self.projectCfg.remoteDir)] == self.projectCfg.remoteDir:
				self.links.append(link)

		self.status = 'parsed'
