"""
Handles storing recieved files.
"""


import re


class storer:


	basePath = ''


	def __init__(self, main):
		self.main = main


	def setBasePath(self, basePath):
		self.basePath = basePath


	def store(self, page, url):
		path = self.basePath + '/' + self.getPath(url)
		self.save(page, path)


	def save(self, page, path):
		contents = page.read()
		dst = file(path, 'w')
		dst.write(contents)
		dst.close()


	def getPath(self, url):
		match = re.search('[^/]+$', url)
		path = match.group(0)
		return path
