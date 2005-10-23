# -*- coding: windows-1251 -*-
"""
Handles GUI.
"""

from Tkinter import *


class Ui(Frame):

	entries = 0

	def __init__(self, main):
		Frame.__init__(self)
		self.main = main
		self.__createWidgets()


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
		self.buttonStart = Button(frameButtons, {'text': 'Start', 'width': 8})

		self.textTable = Text(self, {'height': 5})
		self.textTable.mark_set('last_line', '1.end')
		self.textTable.mark_gravity('last_line', 'right')


		# Pack level 0
		self.pack({'fill': 'both', 'expand': 'yes'});

		# Pack level 1
		self.textTable.pack({'side': 'bottom', 'fill': 'both', 'expand': 'yes'})
		frameParams.pack({'side': 'left', 'fill': 'x', 'expand': 'yes'})
		frameButtons.pack({'side': 'left', 'fill': 'y'})

		# Pack level 2
		self.buttonQuit.pack({'side': 'top', 'fill':'y', 'expand': 'yes'});
		self.buttonStart.pack({'side': 'top', 'fill':'y', 'expand': 'yes'});

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
		self.buttonStart.configure({'command': self.main.controller.getStartController()})
		self.buttonQuit.configure({'command': self.main.controller.getQuitController()})
		self.master.bind('<Escape>', self.main.controller.getQuitController())
		self.entryFirstUrl.bind('<KeyRelease>', self.main.controller.getFirstUrlTypingController())
		self.entryRegExp.bind('<KeyRelease>', self.main.controller.getRegExpTypingController())


	def __setDefaultValues(self):
		self.entryFirstUrl.insert('end', 'http://localhost/index.php')
		self.entryRegExp.insert('end', '^.*$')
		self.entryLocalPath.insert('end', '/usr/!')
		self.entryTestUrl.insert('end', self.entryFirstUrl.get())
		self.main.controller.getRegExpTypingController()()


	def mainloop(self):
		self.__setDefaultValues()
		Frame.mainloop(self)
