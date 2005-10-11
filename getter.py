"""
Handles getting files from internet.
"""


from urllib import *


class getter:
	def get(self, url):
		return urlopen(url)
