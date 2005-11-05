"""
Represents an stored or just queued page.
"""

import urllib

class Page:
	url = None
	path = None
	status = None
	contents = None

	def __init__(self, url, status = 'queued'):
		self.status = status
		self.url = url

	def getContents(self):
		self.contents = urllib.urlopen(self.url).read()

	def setPath(self, path):
		self.path = path

	def setStatus(self, status):
		self.status = status
