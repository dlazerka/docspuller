"""
Handles getting files from internet.
"""


from urllib import *


class getter:
	def __init__(self, main):
		self.main = main

	def get(self, url):
		return urlopen(url)
