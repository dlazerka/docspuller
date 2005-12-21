from Project import Project
import thread


class SiteDownloader(object):
	def __init__(self):
		self.readCfg()
		self.project = self.defProjectData['project']
		self.project.readCfg(self.defProjectData['cfgFileName'])
		self.__isActive = False
		self.activityListeners = []
		self.projectListeners = []


	def readCfg(self):
		import os.path
		import xml.dom.minidom as minidom

		cfgFileName = os.path.dirname(__file__) + '/../SiteDownloader.cfg.xml'

		cfgNode = minidom.parse(cfgFileName).getElementsByTagName('cfg')[0]
		projectsNode = cfgNode.getElementsByTagName('projects')[0]
		projectNodes = projectsNode.getElementsByTagName('project')

		self.projects = []
		self.projectsData = []
		self.defProjectData = None
		for projectNode in projectNodes:
			projectName = projectNode.getElementsByTagName('name')[0].childNodes[0].data
			projectCfgFileName = projectNode.getElementsByTagName('cfgFileName')[0].childNodes[0].data
			projectCfgFileName = os.path.join(os.path.dirname(cfgFileName), projectCfgFileName)
			isDefault = projectNode.getElementsByTagName('isDefault').length == 1

			project = Project(name = projectName)
			projectData = {
				'project': project,
				'cfgFileName': projectCfgFileName,
				'isDefault': isDefault,
			}

			self.projectsData.append(projectData)
			self.projects.append(project)

			if isDefault:
				self.defProjectData = projectData

		if not self.defProjectData:
			self.defProjectData = self.projectsData[0]


	def setProject(self, project):
		i = self.projects.index(project)
		project.readCfg(self.projectsData[i]['cfgFileName'])
		self.project = project
		self.notifyProjectListeners()


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


	def addProjectListener(self, listener):
		self.projectListeners.append(listener)


	def notifyProjectListeners(self):
		for listener in self.projectListeners:
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

