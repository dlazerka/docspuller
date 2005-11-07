from Tkinter import *
from controller import Controller
from model import ProjectFactory


class View:
	widgets = None


	@classmethod
	def show(cls):
		project = ProjectFactory.getCurrentProject()
		project.registerObserver(cls.refreshControls)

		cls.createWidgets()
		cls.bind()
		Frame.mainloop(cls.widgets['mainFrame'])
		Controller.start()


	@classmethod
	def quit(cls, *args):
		cls.widgets['mainFrame'].quit()


	@classmethod
	def createWidgets(cls):
		cls.widgets = dict()
		# Create frames to pack widgets to
		cls.widgets['mainFrame'] = Frame()

		cls.widgets['frameParams'] = Frame(cls.widgets['mainFrame'])
		cls.widgets['frameButtons'] = Frame(cls.widgets['mainFrame'], {'cursor': 'hand2'})

		cls.widgets['frameFirstUrl'] = Frame(cls.widgets['frameParams'])
		cls.widgets['frameLocalPath'] = Frame(cls.widgets['frameParams'])
		cls.widgets['frameRegExp'] = Frame(cls.widgets['frameParams'])
		cls.widgets['frameTestUrl'] = Frame(cls.widgets['frameParams'])
		cls.widgets['frameTestResult'] = Frame(cls.widgets['frameParams'])


		# Create widgets
		cls.widgets['labelFirstUrl'] = Label(cls.widgets['frameFirstUrl'], {'text': 'First Url: '})
		cls.widgets['labelLocalPath'] = Label(cls.widgets['frameLocalPath'], {'text': 'Local Path: '})
		cls.widgets['labelRegExp'] = Label(cls.widgets['frameRegExp'], {'text': 'RegExp: '})
		cls.widgets['labelTestUrl'] = Label(cls.widgets['frameTestUrl'], {'text': 'Test Url: '})
		cls.widgets['labelTestResultLabel'] = Label(cls.widgets['frameTestResult'], {'text': 'Test Result:'})
		cls.widgets['labelTestResult'] = Label(cls.widgets['frameTestResult'])

		cls.widgets['entryFirstUrl'] = Entry(cls.widgets['frameFirstUrl'])
		cls.widgets['entryLocalPath'] = Entry(cls.widgets['frameLocalPath'])
		cls.widgets['entryRegExp'] = Entry(cls.widgets['frameRegExp'])
		cls.widgets['entryTestUrl'] = Entry(cls.widgets['frameTestUrl'])

		cls.widgets['buttonQuit'] = Button(cls.widgets['frameButtons'], {'text': 'Quit', 'width': 8})
		cls.widgets['buttonControl'] = Button(cls.widgets['frameButtons'], {'width': 8})

		cls.widgets['pagesList'] = Text(cls.widgets['mainFrame'], {'height': 5})
		cls.widgets['pagesList'].mark_set('last_line', '1.end')
		cls.widgets['pagesList'].mark_gravity('last_line', 'right')


		# Pack level 0
		cls.widgets['mainFrame'].pack({'fill': 'both', 'expand': 'yes'});

		# Pack level 1
		cls.widgets['pagesList'].pack({'side': 'bottom', 'fill': 'both', 'expand': 'yes'})
		cls.widgets['frameParams'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})
		cls.widgets['frameButtons'].pack({'side': 'left', 'fill': 'y'})

		# Pack level 2
		cls.widgets['buttonQuit'].pack({'side': 'top', 'fill':'y', 'expand': 'yes'});
		cls.widgets['buttonControl'].pack({'side': 'top', 'fill':'y', 'expand': 'yes'});

		cls.widgets['frameFirstUrl'].pack({'side': 'top', 'fill': 'x'})
		cls.widgets['labelFirstUrl'].pack({'side': 'left'})
		cls.widgets['entryFirstUrl'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		cls.widgets['frameLocalPath'].pack({'side': 'top', 'fill': 'x'})
		cls.widgets['labelLocalPath'].pack({'side': 'left'})
		cls.widgets['entryLocalPath'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		cls.widgets['frameRegExp'].pack({'side': 'top', 'fill': 'x'})
		cls.widgets['labelRegExp'].pack({'side': 'left'})
		cls.widgets['entryRegExp'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		cls.widgets['frameTestUrl'].pack({'side': 'top', 'fill': 'x'})
		cls.widgets['labelTestUrl'].pack({'side': 'left'})
		cls.widgets['entryTestUrl'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		cls.widgets['frameTestResult'].pack({'side': 'top', 'fill': 'x'})
		cls.widgets['labelTestResultLabel'].pack({'side': 'left'})
		cls.widgets['labelTestResult'].pack({'side': 'left'})


	@classmethod
	def bind(cls):
		# Binds
		cls.widgets['mainFrame'].master.bind('<Escape>', cls.quit)
		cls.widgets['buttonQuit'].configure({'command': cls.quit})
		cls.widgets['buttonControl'].configure({'command': Controller.start})
		cls.widgets['entryFirstUrl'].bind('<KeyRelease>', Controller.firstUrlTyping)
		cls.widgets['entryRegExp'].bind('<KeyRelease>', Controller.regExpTyping)



	@classmethod
	def refreshControls(cls):
		cls.widgets['mainFrame'].entryTestUrl.insert('end', cls.widgets['mainFrame'].entryFirstUrl.get())
		cls.controller.regExpTyping(cls.widgets['mainFrame'].entryRegExp.get())
		if cls.controller.status == 'inactive':
			cls.widgets['mainFrame'].buttonControl.configure({'text': 'Start', 'command': Controller.start})
			cls.widgets['mainFrame'].entryFirstUrl.configure({'state': 'normal'})
			cls.widgets['mainFrame'].entryLocalPath.configure({'state': 'normal'})
		else:
			cls.widgets['mainFrame'].buttonControl.configure({'text': 'Stop', 'command': Controller.stop})
			cls.widgets['mainFrame'].entryFirstUrl.configure({'state': 'readonly'})
			cls.widgets['mainFrame'].entryLocalPath.configure({'state': 'readonly'})


	@classmethod
	def refreshPage(cls, page):
		if page in cls.widgets['mainFrame'].pagesListed:
			line = cls.widgets['mainFrame'].pagesListed.index(page) + 1
			cls.widgets['mainFrame'].pagesList.delete('%d.0' % line, '%d.end' % line)
		else:
			cls.widgets['mainFrame'].pagesListed.append(page)
			line = len(cls.widgets['mainFrame'].pagesListed)

		cls.widgets['mainFrame'].pagesList.insert('%d.end' % line, '%s    %s' % (page.url, page.status))
		if page.path:
			cls.widgets['mainFrame'].pagesList.insert('%d.end' % line, '    %s' % (page.path))
		cls.widgets['mainFrame'].pagesList.insert('%d.end' % line, '\n')
