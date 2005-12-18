from Project import Project
import thread


class SiteDownloader(object):
	def __init__(self):
		self.readCfg()
		self.project = self.defProject
		self.project.readCfg()
		self.__isActive = False
		self.activityListeners = []


	def readCfg(self):
		import os.path
		import xml.dom.minidom as minidom

		cfgFileName = os.path.dirname(__file__) + '/../SiteDownloader.cfg.xml'

		cfgNode = minidom.parse(cfgFileName).getElementsByTagName('cfg')[0]
		projectsNode = cfgNode.getElementsByTagName('projects')[0]
		projectNodes = projectsNode.getElementsByTagName('project')

		self.projects = []
		self.defProject = None
		for projectNode in projectNodes:
			projectCfgFileName = projectNode.getElementsByTagName('cfgFileName')[0].childNodes[0].data
			projectCfgFileName = os.path.join(os.path.dirname(cfgFileName), projectCfgFileName)

			project = Project(
				cfgFileName = projectCfgFileName,
				isDefault = projectNode.getElementsByTagName('isDefault').length == 1,
			)
			self.projects.append(project)
			if project.isDefault:
				self.defProject = project

		if not self.defProject:
			self.defProject = self.projects[0]


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
		from Project import NoMorePages
		while self.isActive():
			try:
				self.project.storeNextPage()
			except NoMorePages:
				self.stop()
			except Exception:
				self.stop()
				raise

