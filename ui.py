# -*- coding: windows-1251 -*-
"""
Handles GUI.
"""

from Tkinter import *


class Application(Frame):

	entries = 0

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.__createWidgets()
		self.__setBindings()

	def __createWidgets(self):
		self.but1 = Button(self, {'text': 'Quit', 'command': self.quit, 'width': 8})
		self.label1 = Label(self, {'text':'First Page: '})
		self.label2 = Label(self, {'text':'RegExp: '})
		self.entry1 = Entry(self)
		self.entry2 = Entry(self)
		self.text1 = Text(self, {'height': 10})

		self.pack({'fill': 'both', 'expand': 'yes'});
		self.label1.grid({'row': 0, 'column': 0})
		self.label2.grid({'row': 1, 'column': 0})
		self.entry1.grid({'row': 0, 'column': 1, 'sticky': 'we'})
		self.entry2.grid({'row': 1, 'column': 1, 'sticky': 'we'})
		self.but1.grid({'row': 0, 'column': 2, 'rowspan': 2, 'sticky': 'ns'})
		self.text1.grid({'row': 2, 'column': 0, 'columnspan': 3, 'sticky': 'nswe'})
		self.columnconfigure(1, {'weight': 1});
		self.rowconfigure(2, {'weight': 1, 'minsize': '50'});

	def __setBindings(self):
		self.master.bind('<Escape>', lambda event: self.quit())
		self.master.bind('<t>', lambda event: self.addDownloadEntry(name = "t"))

	def addEntry(self, name):
		self.entries += 1
		self.text1.insert('%d.end' % self.entries, '%d: %s\n' % (self.entries, name))


class ui(Application):
	def __init__(self):
		Application.__init__(self)
		self.addEntry('started')
		self.mainloop()
