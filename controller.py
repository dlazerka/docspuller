"""
Implements control functions
"""

class controller:
	def __init__(self, main):
		self.main = main


	def getStartController(self):
		def startController(*args):
			#self.getter.get(entryFirstUrl.get())
			self.main.ui.textTable.insert('0.end', 'kuku\n')

		return startController


	def getQuitController(self):
		def quitController(*args):
			self.main.ui.quit()

		return quitController
