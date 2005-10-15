# -*- coding: windows-1251 -*-
"""
Handles GUI.
"""

from Tkinter import *


class ui(Frame):

	entries = 0

	def __init__(self, main):
		Frame.__init__(self)
		self.main = main
		self.__createWidgets()


	def __createWidgets(self):
		self.buttonQuit = Button(self, {'text': 'Quit', 'width': 8})
		self.buttonStart = Button(self, {'text': 'Start', 'width': 8})

		self.labelFirstUrl = Label(self, {'text':'First Page: '})
		self.labelRegExp = Label(self, {'text':'RegExp: '})
		self.labelLocalPath = Label(self, {'text':'Local Path: '})
		self.labelTestUrl = Label(self, {'text':'Test Url: '})
		self.labelTestUrlResult = Label(self, {'text':'', 'width': 6})

		self.entryFirstUrl = Entry(self)
		self.entryRegExp = Entry(self)
		self.entryLocalPath = Entry(self)
		self.entryTestUrl = Entry(self)
		self.textTable = Text(self, {'height': 10})


		self.buttonStart.configure({'command': self.main.controller.getStartController()})
		self.buttonQuit.configure({'command': self.main.controller.getQuitController()})
		self.master.bind('<Escape>', self.main.controller.getQuitController())
		self.master.bind('<s>', self.main.controller.getStartController())


		self.pack({'fill': 'both', 'expand': 'yes'});
		self.columnconfigure(1, {'weight': 1});
		self.rowconfigure(4, {'weight': 1, 'minsize': '50'});

		self.labelFirstUrl.grid({'row': 0, 'column': 0, })
		self.entryFirstUrl.grid({'row': 0, 'column': 1, 'columnspan': 2, 'sticky': 'we'})
		self.buttonQuit.grid({'row': 0, 'column': 3, 'rowspan': 2, 'sticky': 'ns'})
		self.labelRegExp.grid({'row': 1, 'column': 0, })
		self.entryRegExp.grid({'row': 1, 'column': 1, 'columnspan': 2, 'sticky': 'we'})
		self.labelLocalPath.grid({'row': 2, 'column': 0, })
		self.entryLocalPath.grid({'row': 2, 'column': 1, 'columnspan': 2, 'sticky': 'we'})
		self.buttonStart.grid({'row': 2, 'column': 3, 'rowspan': 2, 'sticky': 'ns'})
		self.labelTestUrl.grid({'row': 3, 'column': 0, })
		self.entryTestUrl.grid({'row': 3, 'column': 1, 'sticky': 'we'})
		self.labelTestUrlResult.grid({'row': 3, 'column': 2, })
		self.textTable.grid({'row': 4, 'column': 0, 'columnspan': 4, 'sticky': 'nswe'})

		self.entryFirstUrl.insert('end', 'http://localhost/index.php')
		self.entryRegExp.insert('end', '.*')
		self.entryLocalPath.insert('end', '/usr/!')
		self.entryTestUrl.insert('end', self.entryFirstUrl.get())
