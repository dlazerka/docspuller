import xml.dom.minidom
import re

import Listened


class ProjectCfg:
	def __init__(self, name, filePath):
		self.filePath = filePath
		self.name = name
		self.firstUrl = None
		self.localDir = None
		self.remoteDir = None
		self.regExp = None
		self.__isLoaded = False


	def load(self):
		self.cfgDOM = xml.dom.minidom.parse(self.filePath)
		cfgNode = self.cfgDOM.getElementsByTagName('cfg')[0]

		self.name = cfgNode.getElementsByTagName('name')[0].childNodes[0].data
		self.firstUrl = cfgNode.getElementsByTagName('firstUrl')[0].childNodes[0].data
		self.remoteDir = cfgNode.getElementsByTagName('remoteDir')[0].childNodes[0].data
		self.localDir = cfgNode.getElementsByTagName('localDir')[0].childNodes[0].data
		self.regExp = cfgNode.getElementsByTagName('regExp')[0].childNodes[0].data

		self.__isLoaded = True


	def set(self,
		name = None,
		firstUrl = None,
		localDir = None,
		remoteDir = None,
		regExp = None,
	):
		if name:
			self.name = name
		if firstUrl:
			self.firstUrl = firstUrl
		if localDir:
			self.localDir = localDir
		if regExp:
			self.regExp = regExp

		if firstUrl:
			if not remoteDir:
				self.remoteDir = re.sub('/[^/]*$', '', firstUrl)

		self.notifyListeners(
			name = name,
			firstUrl = firstUrl,
			localDir = localDir,
			remoteDir = remoteDir,
			regExp = regExp,
		)


	def save(self):
		string = StringIO()
		def Dom2String(dom, string, currentNode = None):
			return string.dom.toxml()

		f = file(self.filePath + '.cpy', 'w')
		f.write(string)
		f.close()


	def isLoaded(self):
		return self.__isLoaded


	addListener = Listened.getAddListenerMethod('')
	notifyListeners = Listened.getNotifyListenersMethod('')


