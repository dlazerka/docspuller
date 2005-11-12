import model as MODEL


class _Controller:
	status = 'inactive'


	def start(self, **args):
		self.status = 'active'

		import re
		MODEL.Project.settings['remoteDir'] = re.sub('/[^/]*$', '', args['firstUrl'])
		MODEL.Project.settings['localDir'] = args['localDir']
		MODEL.Project.settings['regExp'] = args['regExp']

		MODEL.Project.addUrl(args['firstUrl'])

		import thread
		thread.start_new_thread(self.__loop, ())


	def stop(self, *args):
		self.main.status = 'inactive'


	def __loop(self):
		while self.status == 'active':
			try:
				page = MODEL.Project.storeNextPage()
			except MODEL.NoMorePages:
				return


CONTROLLER = _Controller()