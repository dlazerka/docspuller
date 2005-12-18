from PagesContainer import PagesContainer, NoMorePages
from Page import Page


class Project(object):
	def __init__(self, cfgFileName, isDefault = False):
		self.cfgFileName = cfgFileName
		self.isDefault = isDefault
		self.pagesContainer = PagesContainer()


	def readCfg(self):
		import xml.dom.minidom as minidom
		cfgNode = minidom.parse(self.cfgFileName).getElementsByTagName('cfg')[0]


		self.cfg = {}
		self.cfg['name'] = cfgNode.getElementsByTagName('name')[0].childNodes[0].data
		self.cfg['firstUrl'] = cfgNode.getElementsByTagName('firstUrl')[0].childNodes[0].data
		self.cfg['remoteDir'] = cfgNode.getElementsByTagName('remoteDir')[0].childNodes[0].data
		self.cfg['localDir'] = cfgNode.getElementsByTagName('localDir')[0].childNodes[0].data
		self.cfg['regExp'] = cfgNode.getElementsByTagName('regExp')[0].childNodes[0].data


	def setCfg(self, **args):
		import re

		for argName in args:
			self.cfg[argName] = args[argName]
		if 'firstUrl' in args:
			if 'remoteDir' not in args:
				self.cfg['remoteDir'] = re.sub('/[^/]*$', '', args['firstUrl'])
			self.addUrl(args['firstUrl'])


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

