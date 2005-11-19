from PagesContainer import *
from Page import *


class Project:
	settings = {
		'remoteDir': None,
		'localDir': None,
		'regExp': None,
	}
	pagesContainer = None


	def __init__(self):
		self.settings['remoteDir'] = 'http://localhost/common'
		self.settings['localDir'] = '/usr/work/@my/python/SiteDownloader'
		self.settings['regExp'] = '^.*$'
		self.pagesContainer = PagesContainer()


	def addUrl(self, url):
		page = Page(url, self.settings)
		self.pagesContainer.add(page)


	def storeNextPage(self):
		page = self.pagesContainer.popQueued()
		if page.fetchContents():
			page.saveContents()
			page.parse()
			for link in page.links:
				self.addUrl(link)

