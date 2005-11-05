# -*- coding: windows-1251 -*-
"""
Handles GUI.
"""

from Tkinter import *


class Ui(Frame):

	pagesListed = []

	def __init__(self, main):
		Frame.__init__(self)
		self.main = main
		self.__createWidgets()
		self.refresh()


	def mainloop(self):
		self.__setDefaultValues()
		Frame.mainloop(self)


	def __createWidgets(self):

		# Create frames to pack widgets to
		frameParams = Frame(self)
		frameButtons = Frame(self, {'cursor': 'hand2'})

		frameFirstUrl = Frame(frameParams)
		frameLocalPath = Frame(frameParams)
		frameRegExp = Frame(frameParams)
		frameTestUrl = Frame(frameParams)
		frameTestResult = Frame(frameParams)


		# Create widgets
		self.labelFirstUrl = Label(frameFirstUrl, {'text': 'First Url: '})
		self.labelLocalPath = Label(frameLocalPath, {'text': 'Local Path: '})
		self.labelRegExp = Label(frameRegExp, {'text': 'RegExp: '})
		self.labelTestUrl = Label(frameTestUrl, {'text': 'Test Url: '})
		self.labelTestResultLabel = Label(frameTestResult, {'text': 'Test Result:'})
		self.labelTestResult = Label(frameTestResult)

		self.entryFirstUrl = Entry(frameFirstUrl)
		self.entryLocalPath = Entry(frameLocalPath)
		self.entryRegExp = Entry(frameRegExp)
		self.entryTestUrl = Entry(frameTestUrl)

		self.buttonQuit = Button(frameButtons, {'text': 'Quit', 'width': 8})
		self.buttonControl = Button(frameButtons, {'width': 8})

		self.pagesList = Text(self, {'height': 5})
		self.pagesList.mark_set('last_line', '1.end')
		self.pagesList.mark_gravity('last_line', 'right')


		# Pack level 0
		self.pack({'fill': 'both', 'expand': 'yes'});

		# Pack level 1
		self.pagesList.pack({'side': 'bottom', 'fill': 'both', 'expand': 'yes'})
		frameParams.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})
		frameButtons.pack({'side': 'left', 'fill': 'y'})

		# Pack level 2
		self.buttonQuit.pack({'side': 'top', 'fill':'y', 'expand': 'yes'});
		self.buttonControl.pack({'side': 'top', 'fill':'y', 'expand': 'yes'});

		frameFirstUrl.pack({'side': 'top', 'fill': 'x'})
		self.labelFirstUrl.pack({'side': 'left'})
		self.entryFirstUrl.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		frameLocalPath.pack({'side': 'top', 'fill': 'x'})
		self.labelLocalPath.pack({'side': 'left'})
		self.entryLocalPath.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		frameRegExp.pack({'side': 'top', 'fill': 'x'})
		self.labelRegExp.pack({'side': 'left'})
		self.entryRegExp.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		frameTestUrl.pack({'side': 'top', 'fill': 'x'})
		self.labelTestUrl.pack({'side': 'left'})
		self.entryTestUrl.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})

		frameTestResult.pack({'side': 'top', 'fill': 'x'})
		self.labelTestResultLabel.pack({'side': 'left'})
		self.labelTestResult.pack({'side': 'left'})


		# Binds
		self.buttonControl.configure({'command': self.main.controller.getStart()})
		self.buttonQuit.configure({'command': self.main.controller.getQuit()})
		self.master.bind('<Escape>', self.main.controller.getQuit())
		self.entryFirstUrl.bind('<KeyRelease>', self.main.controller.getFirstUrlTyping())
		self.entryRegExp.bind('<KeyRelease>', self.main.controller.getRegExpTyping())


	def refresh(self):
		if self.main.status == 'inactive':
			self.buttonControl.configure({'text': 'Start', 'command': self.main.controller.getStart()})
			self.entryFirstUrl.configure({'state': 'normal'})
			self.entryLocalPath.configure({'state': 'normal'})
		else:
			self.buttonControl.configure({'text': 'Stop', 'command': self.main.controller.getStop()})
			self.entryFirstUrl.configure({'state': 'readonly'})
			self.entryLocalPath.configure({'state': 'readonly'})


	def refreshPage(self, page):
		if page in self.pagesListed:
			line = self.pagesListed.index(page) + 1
			self.pagesList.delete('%d.0' % line, '%d.end' % line)
		else:
			self.pagesListed.append(page)
			line = len(self.pagesListed)

		self.pagesList.insert('%d.end' % line, '%s    %s' % (page.url, page.status))
		if page.path:
			self.pagesList.insert('%d.end' % line, '    %s' % (page.path))
		self.pagesList.insert('%d.end' % line, '\n')




	def __setDefaultValues(self):
		self.entryFirstUrl.insert('end', 'http://localhost/common/sd.php')
		self.entryRegExp.insert('end', '^.*$')
		self.entryLocalPath.insert('end', '/usr/!')
		self.entryTestUrl.insert('end', self.entryFirstUrl.get())
		self.main.controller.getRegExpTyping()()
