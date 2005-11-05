"""
Implements control functions
"""


import re
import time
import thread
from page import *


class Controller:
	def __init__(self, main):
		self.main = main


	def getPage(self, url):
		self.main.ui.textTable.insert('last_line', '%s\tkuku\n' % url)

		page = self.main.getter.get(url)

		self.main.storer.store(page, url)

		return self.main.pageParser.parse(page)


	def getQuit(self):
		def quit(*args):
			self.main.ui.quit()

		return quit


	def getStart(self):
		def start(*args):
			self.main.setStatus('active')

			url = self.main.ui.entryFirstUrl.get()
			localPath = self.main.ui.entryLocalPath.get()
			regExp = self.main.ui.entryRegExp.get()

			self.main.storer.setBasePath(localPath)
			self.main.pageParser.setRegExp(regExp)
			page = self.main.storer.queue(url)

			self.main.ui.refresh()
			self.main.ui.refreshPage(page)

			thread.start_new_thread(self.__loop, ())

		return start


	def __loop(self):
		while self.main.status == 'active':
			page = self.main.storer.storeNext()
			if page:
				self.main.ui.refreshPage(page)
			else:
				self.getStop()()


	def getStop(self):
		def stop(*args):
			self.main.status = 'inactive'

			self.main.ui.refresh()

		return stop


	def getFirstUrlTyping(self):
		def firstUrlTyping(*args):
			firstUrl = self.main.ui.entryFirstUrl.get()
			self.main.ui.entryTestUrl.delete('0', 'end')
			self.main.ui.entryTestUrl.insert('end', firstUrl)
		return firstUrlTyping


	def getRegExpTyping(self):
		def regExpTyping(*args):
			regExp = self.main.ui.entryRegExp.get()
			testUrl = self.main.ui.entryTestUrl.get()

			try:
				re.compile(regExp)
			except re.error, inst:
				text = inst.__str__()
				fg = 'red'
			else:
				if (re.search(regExp, testUrl)):
					text =  'True'
					fg = '#080'
				else:
					text =  'False'
					fg = 'red'

			self.main.ui.labelTestResult.configure({'fg': fg, 'text': text})

		return regExpTyping
