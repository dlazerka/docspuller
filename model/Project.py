from PagesContainer import PagesContainer, NoMorePages
from Page import Page


class Project(object):
	settings = {
		'remoteDir': None,
		'localDir': None,
		'regExp': None,
	}
	pagesContainer = None


	def __init__(self):
		self.settings['remoteDir'] = 'http://localhost/common/'
		self.settings['localDir'] = '/usr/work/@my/python/SiteDownloader/!'
		self.settings['regExp'] = '^[^_]*$'
		self.pagesContainer = PagesContainer()


	def getPages(self):
		return self.pagesContainer.pages

	pages = property(getPages)


	def addUrl(self, url, parentPage = None):
		page = Page(url, self.settings, parentPage)
		self.pagesContainer.add(page)


	def storeNextPage(self):
		page = self.pagesContainer.popQueued()

		if page.fetchContents():
			page.saveContents()
			page.parse()

			import re
			for link in page.links:
				if not self.pagesContainer.containsUrl(link):
					self.addUrl(link, page)

