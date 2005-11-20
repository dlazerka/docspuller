from Project import Project
import thread


class SiteDownloader(object):
	def __init__(self):
		self.project = Project()
		self.__isActive = False
		self.activityListeners = []


	def isActive(self):
		return self.__isActive


	def start(self):
		self.__isActive = True
		self.notifyActivityListeners()
		self.__mainLoopThread = thread.start_new_thread(self.__mainLoop, ())


	def stop(self):
		self.__isActive = False
		self.notifyActivityListeners()


	def addActivityListener(self, listener):
		self.activityListeners.append(listener)

	def notifyActivityListeners(self):
		for listener in self.activityListeners:
			listener()


	def __mainLoop(self):
		from PagesContainer import NoMorePages
		while self.isActive():
			try:
				page = self.project.storeNextPage()
			except NoMorePages:
				self.stop()
			except Exception:
				self.stop()
				raise

