import model.MODEL as MODEL


def start(**args):
	project = MODEL.siteDownloader.project

	import re
	project.settings['remoteDir'] = re.sub('/[^/]*$', '', args['firstUrl'])
	project.settings['localDir'] = args['localDir']
	project.settings['regExp'] = args['regExp']

	project.addUrl(args['firstUrl'])

	MODEL.siteDownloader.start()


def stop(**args):
	MODEL.siteDownloader.stop()

