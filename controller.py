from model import *


class Controller:
	status = 'inactive'


	@classmethod
	def start(cls, *args):
		cls.status = 'active'

		project = ProjectFactory.getCurrentProject()
		page = Page(project.)


		cls.main.ui.refresh()
		cls.main.ui.refreshPage(page)

		cls.__loop()

		#thread.start_new_thread(cls.__loop, ())


	@classmethod
	def stop(*args):
		cls.main.status = 'inactive'

		cls.main.ui.refresh()


	@classmethod
	def __loop(cls):
		try:
			while cls.status == 'active':
				page = cls.main.storer.storeNext()
				if page:
					cls.main.ui.refreshPage(page)
				else:
					cls.stop()
		except Exception, e:
			print id(e)


	@classmethod
	def firstUrlTyping(*args):
		firstUrl = cls.main.ui.entryFirstUrl.get()
		cls.main.ui.entryTestUrl.delete('0', 'end')
		cls.main.ui.entryTestUrl.insert('end', firstUrl)


	@classmethod
	def regExpTyping(cls, *args):
		return
		regExp = Ui.entryRegExp.get()
		testUrl = cls.main.ui.entryTestUrl.get()

		try:
			re.compile(regExp)
		except re.error, inst:
			text = inst.__str__()
			fg = 'red'
		else:
			if (re.search(regExp, testUrl)):
				text =  'True'
				fg = '#080'
			else:
				text =  'False'
				fg = 'red'

		cls.main.ui.labelTestResult.configure({'fg': fg, 'text': text})