from SDStatus import *
from Project import *


class SiteDownloader(object):
	"""
		__mainLoopThread
		project
		status
	"""


	def __init__(self):
		self.project = Project()


	def activeCycle(self):
		import thread
		self.__mainLoopThread = thread.start_new_thread(self.__mainLoop, ())


	def __mainLoop(self):
		while self.status == 'active':
			try:
				page = self.project.storeNextPage()
			except NoMorePages:
				self.status = 'inactive'




	status = SDStatus(activeCycle)
