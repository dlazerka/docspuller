import model.MODEL as MODEL


def start(firstUrl, localDir, regExp):
	project = MODEL.siteDownloader.project

	project.setCfg(
		firstUrl = firstUrl,
		localDir = localDir,
		regExp = regExp,
	)

	MODEL.siteDownloader.start()


def saveProject(self, name, firstUrl, localDir, regExp):
	MODEL.siteDownloader.project.setCfg(
		name = name,
		firstUrl = firstUrl,
		localDir = localDir,
		regExp = regExp,
	)
	MODEL.siteDownloader.project.save()


def toPrevProject(**args):
	__toProject(-1)


def toNextProject(**args):
	__toProject(1)


def __toProject(shift):
	curNum = MODEL.siteDownloader.projects.index(MODEL.siteDownloader.project)
	MODEL.siteDownloader.setProject(MODEL.siteDownloader.projects[curNum + shift])
