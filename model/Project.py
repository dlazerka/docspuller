from PagesContainer import PagesContainer, NoMorePages
from Page import Page


class Project(object):
	def __init__(self, name, isDefault = False):
		self.cfg = {}
		self.cfg['name'] = name
		self.isDefault = isDefault
		self.pagesContainer = PagesContainer()


	def readCfg(self, cfgFileName):
		import xml.dom.minidom as minidom
		cfgNode = minidom.parse(cfgFileName).getElementsByTagName('cfg')[0]

		self.cfg = {}
		self.cfg['name'] = cfgNode.getElementsByTagName('name')[0].childNodes[0].data
		self.cfg['firstUrl'] = cfgNode.getElementsByTagName('firstUrl')[0].childNodes[0].data
		self.cfg['remoteDir'] = cfgNode.getElementsByTagName('remoteDir')[0].childNodes[0].data
		self.cfg['localDir'] = cfgNode.getElementsByTagName('localDir')[0].childNodes[0].data
		self.cfg['regExp'] = cfgNode.getElementsByTagName('regExp')[0].childNodes[0].data


	def saveCfg(self, cfgFileName):
		pass


	def setCfg(self,
		name = None,
		firstUrl = None,
		localDir = None,
		remoteDir = None,
		regExp = None,
	):
		import re
		if name:
			self.cfg['name'] = name
		if firstUrl:
			self.cfg['firstUrl'] = firstUrl
		if localDir:
			self.cfg['localDir'] = localDir
		if regExp:
			self.cfg['regExp'] = regExp
			
		if firstUrl:
			if not remoteDir:
				self.cfg['remoteDir'] = re.sub('/[^/]*$', '', firstUrl)
			self.addUrl(firstUrl)


	def addUrl(self, url, parentPage = None):
		if not self.pagesContainer.containsUrl(url):
			page = Page(url, self.cfg, parentPage)
			self.pagesContainer.add(page)


	def storeNextPage(self):
		page = self.pagesContainer.popQueued()
		if page.fetchContents():
			page.saveContents()
			page.parse()
			for link in page.links:
				self.addUrl(link, page)

