import model.MODEL as MODEL


def start(**args):
	project = MODEL.siteDownloader.project

	project.setCfg(
		firstUrl = args['firstUrl'],
		localDir = args['localDir'],
		regExp = args['regExp'],
	)

	MODEL.siteDownloader.start()


def stop(**args):
	MODEL.siteDownloader.stop()

