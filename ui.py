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
		self.buttonQuit = Button(self, {'text': 'Quit', 'width': 8})
		self.buttonStart = Button(self, {'text': 'Start', 'width': 8})

		self.labelFirstUrl = Label(self, {'text': 'First Url: '})
		self.labelRegExp = Label(self, {'text': 'RegExp: '})
		self.labelLocalPath = Label(self, {'text': 'Local Path: '})
		self.labelTestUrl = Label(self, {'text': 'Test Url: '})
		self.labelTestResultLabel = Label(self, {'text': 'Test Result:', 'justify' : 'left'})
		self.labelTestResult = Label(self, {})

		self.entryFirstUrl = Entry(self)
		self.entryRegExp = Entry(self)
		self.entryLocalPath = Entry(self)
		self.entryTestUrl = Entry(self)
		self.textTable = Text(self, {'height': 10})
		self.textTable.mark_set('last_line', '1.end')
		self.textTable.mark_gravity('last_line', 'right')


		self.buttonStart.configure({'command': self.main.controller.getStartController()})
		self.buttonQuit.configure({'command': self.main.controller.getQuitController()})
		self.master.bind('<Escape>', self.main.controller.getQuitController())
		self.entryFirstUrl.bind('<KeyRelease>', self.main.controller.getFirstUrlTypingController())
		self.entryRegExp.bind('<KeyRelease>', self.main.controller.getRegExpTypingController())


		self.pack({'fill': 'both', 'expand': 'yes'});
		self.columnconfigure(1, {'weight': 1});
		self.rowconfigure(5, {'weight': 1, 'minsize': '50'});

		self.labelFirstUrl.grid({'row': 0, 'column': 0, })
		self.entryFirstUrl.grid({'row': 0, 'column': 1, 'sticky': 'we'})
		self.buttonQuit.grid({'row': 0, 'column': 3, 'rowspan': 2, 'sticky': 'ns'})
		self.labelLocalPath.grid({'row': 1, 'column': 0, })
		self.entryLocalPath.grid({'row': 1, 'column': 1, 'sticky': 'we'})
		self.labelRegExp.grid({'row': 2, 'column': 0, })
		self.entryRegExp.grid({'row': 2, 'column': 1, 'sticky': 'we'})
		self.buttonStart.grid({'row': 2, 'column': 3, 'rowspan': 2, 'sticky': 'ns'})
		self.labelTestUrl.grid({'row': 3, 'column': 0, })
		self.entryTestUrl.grid({'row': 3, 'column': 1, 'sticky': 'we'})
		self.labelTestUrl.grid({'row': 3, 'column': 0})
		self.labelTestResultLabel.grid({'row': 4, 'column': 0, 'sticky': 'we'})
		self.labelTestResult.grid({'row': 4, 'column': 1, 'sticky': 'we'})
		self.textTable.grid({'row': 5, 'column': 0, 'columnspan': 4, 'sticky': 'nswe'})

	def __setDefaultValues(self):
		self.entryFirstUrl.insert('end', 'http://localhost/index.php')
		self.entryRegExp.insert('end', '^.*$')
		self.entryLocalPath.insert('end', '/usr/!')
		self.entryTestUrl.insert('end', self.entryFirstUrl.get())
		self.main.controller.getRegExpTypingController()()

	def mainloop(self):
		self.__setDefaultValues()
		Frame.mainloop(self)
