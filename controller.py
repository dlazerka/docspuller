"""
Implements control functions
"""


import re


class Controller:
	def __init__(self, main):
		self.main = main


	def getQuitController(self):
		def quitController(*args):
			self.main.ui.quit()

		return quitController


	def getStartController(self):
		def startController(*args):
			url = self.main.ui.entryFirstUrl.get()
			localPath = self.main.ui.entryLocalPath.get()
			regExp = self.main.ui.entryRegExp.get()

			self.main.ui.entryFirstUrl.configure({'state': 'readonly'})
			self.main.ui.entryLocalPath.configure({'state': 'readonly'})

			self.main.storer.setBasePath(localPath)
			self.main.parser.setRegExp(regExp)

			self.main.ui.textTable.insert('last_line', 'kuku')
			page = self.main.getter.get(url)
			self.main.storer.store(page, url)

		return startController

	def getFirstUrlTypingController(self):
		def firstUrlTypingController(*args):
			firstUrl = self.main.ui.entryFirstUrl.get()
			self.main.ui.entryTestUrl.delete('0', 'end')
			self.main.ui.entryTestUrl.insert('end', firstUrl)
		return firstUrlTypingController


	def getRegExpTypingController(self):
		def regExpTypingController(*args):
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

		return regExpTypingController
