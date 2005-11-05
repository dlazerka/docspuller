"""
Handles storing recieved files.
"""


import re
from page import *


class Storer:
	pages = []
	pagesQueued = []

	def __init__(self, main):
		self.main = main


	def setBasePath(self, basePath):
		if (basePath[-1:] == '/'):
			self.basePath = basePath[0:-1]
		else:
			self.basePath = basePath


	def queue(self, url):
		page = Page(url)
		self.pagesQueued.append(page)

		return page


	def storeNext(self):
		if self.pagesQueued == []:
			return False

		page = self.pagesQueued.pop(0)
		page.path = self.basePath + '/' + self.__pagePath(page.url)

		page.getContents()

		dst = file(page.path, 'w')
		dst.write(page.contents)
		dst.close()
		delattr(page, 'contents')

		page.setStatus('stored')

		return page


	def __pagePath(self, url):
		match = re.search('[^/]+$', url)
		path = match.group(0)
		return path
