from Tkinter import *
from tkFont import *
import re

import controller.CONTROLLER as CONTROLLER
import model.MODEL as MODEL
#from model.Status import Status


class Ui:
	def show(self):
		self.widgets = dict()
		self.fonts = dict()
		self.pagesShown = []
		self.tk = Tk()
		self.firstUrl = 'http://localhost/common/tutorial/httpscripting.html'

		self.createWidgets()
		self.bind()
		self.refreshControls()
		self.regExpTyping()
		MODEL.siteDownloader.addActivityListener(self.refreshControls)
		MODEL.siteDownloader.project.pagesContainer.addNewPageListener(self.addPage)

		#self.actStart()

		Frame.mainloop(self.widgets['mainFrame'])



	def quit(self, *args):
		self.widgets['mainFrame'].quit()


	def bind(self):
		# Binds
		self.widgets['mainFrame'].master.bind('<Escape>', self.quit)
		self.widgets['checkbuttonShowAllPages'].configure({'command': self.refreshPagesList})
		self.widgets['buttonQuit'].configure({'command': self.quit})
		self.widgets['buttonControl'].configure({'command': self.actStart})
		self.widgets['entryRegExp'].bind('<KeyRelease>', self.regExpTyping)


	def actStart(self):
		localDir = self.widgets['entryLocalDir'].get()
		self.firstUrl = self.widgets['entryFirstUrl'].get()
		regExp = self.widgets['entryRegExp'].get()
		CONTROLLER.start(localDir = localDir, firstUrl = self.firstUrl, regExp = regExp)
		#self.refreshControls()


	def actStop(self):
		pass


	def refreshControls(self):
		if MODEL.siteDownloader.isActive():
			self.widgets['buttonControl'].configure({'text': 'Stop', 'command': self.actStop})
			self.widgets['entryFirstUrl'].configure({'state': 'readonly'})
			self.widgets['entryLocalDir'].configure({'state': 'readonly'})
		else:
			self.widgets['buttonControl'].configure({'text': 'Start', 'command': self.actStart})
			self.widgets['entryFirstUrl'].configure({'state': 'normal'})
			self.widgets['entryLocalDir'].configure({'state': 'normal'})

		project = MODEL.siteDownloader.project
		self.widgets['entryFirstUrl'].delete('0', 'end')
		self.widgets['entryLocalDir'].delete('0', 'end')
		self.widgets['entryRegExp'].delete('0', 'end')
		self.widgets['entryTestUrl'].delete('0', 'end')
		self.widgets['entryFirstUrl'].insert('0', self.firstUrl)
		self.widgets['entryLocalDir'].insert('0', project.settings['localDir'])
		self.widgets['entryRegExp'].insert('0', project.settings['regExp'])
		self.widgets['entryTestUrl'].insert('0', self.widgets['entryFirstUrl'].get())


	def addPage(self, page):
		if page.status == 'failed regexp' and not self.widgets['checkbuttonShowAllPages'].isSelected.get():
			return

		page.addStatusListener(self.pageStatusChanged)

		lineStart = self.widgets['pagesList'].index('End')

		self.widgets['pagesList'].insert('End', '%s ' % page.id);
		if page.parent:
			self.widgets['pagesList'].insert('End', '%s ' % page.parent.id);
		self.widgets['pagesList'].insert('End', page.url);
		self.widgets['pagesList'].insert('End', '  ->  ');
		self.widgets['pagesList'].insert('End', page.relPath);
		self.widgets['pagesList'].insert('End', '    ');

		self.widgets['pagesList'].mark_set('Page%sStatusStart' % id(page), 'End')
		self.widgets['pagesList'].mark_gravity('Page%sStatusStart' % id(page), 'left')
		self.widgets['pagesList'].insert('End', page.status);
		self.widgets['pagesList'].mark_set('Page%sStatusEnd' % id(page), 'End')
		self.widgets['pagesList'].mark_gravity('Page%sStatusEnd' % id(page), 'left')
		self.widgets['pagesList'].insert('End', '\n');
		self.widgets['pagesList'].mark_gravity('Page%sStatusEnd' % id(page), 'right')


		self.widgets['pagesList'].tag_add('Page%s' % id(page), lineStart, 'End');

		if page.status == 'failed regexp':
			self.widgets['pagesList'].tag_configure('Page%s' % id(page), {
				'background': '#eeeeee',
			});


	def pageStatusChanged(self, page):
		self.widgets['pagesList'].delete('Page%sStatusStart' % id(page), 'Page%sStatusEnd' % id(page));
		self.widgets['pagesList'].insert('Page%sStatusStart' % id(page), page.status);


	def refreshPagesList(self):
		self.clearPages()
		for page in MODEL.siteDownloader.project.pages:
			self.addPage(page)


	def clearPages(self):
		self.widgets['pagesList'].delete('1.0', 'End')
		self.pagesCnt = 0



	def regExpTyping(self, *args):
		regExp = self.widgets['entryRegExp'].get()
		testUrl = self.widgets['entryTestUrl'].get()

		try:
			re.compile(regExp)
		except re.error, e:
			text = e.__str__()
			fg = 'red'
		else:
			if (re.search(regExp, testUrl)):
				text =  'True'
				fg = '#080'
			else:
				text =  'False'
				fg = 'red'

		self.widgets['labelTestResult'].configure({'fg': fg, 'text': text})


	def createWidgets(self):
		# Create frames to pack widgets to
		self.widgets['mainFrame'] = Frame(self.tk)

		self.widgets['frameParams'] = Frame(self.widgets['mainFrame'])
		self.widgets['frameCheckboxes'] = Frame(self.widgets['mainFrame'])
		self.widgets['frameButtons'] = Frame(self.widgets['mainFrame'], {
			'cursor': 'hand2',
		})

		self.widgets['frameFirstUrl'] = Frame(self.widgets['frameParams'])
		self.widgets['frameLocalDir'] = Frame(self.widgets['frameParams'])
		self.widgets['frameRegExp'] = Frame(self.widgets['frameParams'])
		self.widgets['frameTestUrl'] = Frame(self.widgets['frameParams'])
		self.widgets['frameTestResult'] = Frame(self.widgets['frameParams'])


		# Create widgets
		self.widgets['labelFirstUrl'] = Label(self.widgets['frameFirstUrl'], {
			'text': 'First Url: '
		})
		self.widgets['labelLocalDir'] = Label(self.widgets['frameLocalDir'], {
			'text': 'Local Path: '
		})
		self.widgets['labelRegExp'] = Label(self.widgets['frameRegExp'], {
			'text': 'RegExp: '
		})
		self.widgets['labelTestUrl'] = Label(self.widgets['frameTestUrl'], {
			'text': 'Test Url: '
		})
		self.widgets['labelTestResultLabel'] = Label(self.widgets['frameTestResult'], {
			'text': 'Test Result:'
		})
		self.widgets['labelTestResult'] = Label(self.widgets['frameTestResult'], {
		})

		self.widgets['entryFirstUrl'] = Entry(self.widgets['frameFirstUrl'])
		self.widgets['entryLocalDir'] = Entry(self.widgets['frameLocalDir'])
		self.widgets['entryRegExp'] = Entry(self.widgets['frameRegExp'])
		self.widgets['entryTestUrl'] = Entry(self.widgets['frameTestUrl'])

		self.widgets['checkbuttonShowAllPages'] = Checkbutton(self.widgets['frameCheckboxes'], {
			'text': 'Show All Pages',
			'pady': 3,
			'cursor': 'hand2',
		})
		self.widgets['checkbuttonShowAllPages'].isSelected = IntVar()
		self.widgets['checkbuttonShowAllPages'].configure({
			'variable': self.widgets['checkbuttonShowAllPages'].isSelected,
		})

		self.widgets['buttonQuit'] = Button(self.widgets['frameButtons'], {
			'text': 'Quit',
			'width': 8
		})
		self.widgets['buttonControl'] = Button(self.widgets['frameButtons'], {
			'width': 8
		})

		self.fonts['pagesList'] = Font(self.tk,
			size = 10,
			family = 'Courier',
			weight = 'bold'
		)
		self.widgets['pagesList'] = Text(self.widgets['mainFrame'], {
			'width': 100,
			'height': 20,
			'font': self.fonts['pagesList']
		})
		self.widgets['pagesList'].mark_set('End', '1.end')
		self.widgets['pagesList'].mark_gravity('End', 'right')



		# Pack level 0
		self.widgets['mainFrame'].pack({'fill': 'both', 'expand': 'yes'});


		# Pack level 1
		self.widgets['pagesList'].pack({'side': 'bottom', 'fill': 'both', 'expand': 'yes'})
		self.widgets['frameParams'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})
		self.widgets['frameCheckboxes'].pack({'side': 'left', 'fill': 'y'})
		self.widgets['frameButtons'].pack({'side': 'left', 'fill': 'y'})


		# Pack level 2
		self.widgets['frameFirstUrl'].pack({'side': 'top', 'fill': 'x'})
		self.widgets['labelFirstUrl'].pack({'side': 'left'})
		self.widgets['entryFirstUrl'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		self.widgets['frameLocalDir'].pack({'side': 'top', 'fill': 'x'})
		self.widgets['labelLocalDir'].pack({'side': 'left'})
		self.widgets['entryLocalDir'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		self.widgets['frameRegExp'].pack({'side': 'top', 'fill': 'x'})
		self.widgets['labelRegExp'].pack({'side': 'left'})
		self.widgets['entryRegExp'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		self.widgets['frameTestUrl'].pack({'side': 'top', 'fill': 'x'})
		self.widgets['labelTestUrl'].pack({'side': 'left'})
		self.widgets['entryTestUrl'].pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		self.widgets['frameTestResult'].pack({'side': 'top', 'fill': 'x'})
		self.widgets['labelTestResultLabel'].pack({'side': 'left'})
		self.widgets['labelTestResult'].pack({'side': 'left'})

		self.widgets['checkbuttonShowAllPages'].pack({'side': 'top'})

		self.widgets['buttonQuit'].pack({'side': 'top', 'fill':'y', 'expand': 'yes'});
		self.widgets['buttonControl'].pack({'side': 'top', 'fill':'y', 'expand': 'yes'});


ui = Ui()
