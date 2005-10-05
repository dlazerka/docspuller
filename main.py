from Tkinter import *
def v(val):
	print val

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	def exit(self, event):
		self.quit()

	def createWidgets(self):
		#self.canvas1 = Canvas(self, {})
		#self.canvas2 = Canvas(self, {})
		#self.but1 = Button(self.canvas2, {'width': 5, 'height':2, 'text': 'Quit', 'command': self.quit})
		#self.label1 = Label(self.canvas1, {'text':'First Page: '})
		#self.label2 = Label(self.canvas1, {'text':'RegExp: '})
		#self.entry1 = Entry(self.canvas1, {'width': 30})
		#self.entry2 = Entry(self.canvas1, {'width': 30})
		self.but1 = Button(self, {'text': 'Quit', 'command': self.quit, 'width': 5, 'height':2})
		self.label1 = Label(self, {'text':'First Page: '})
		self.label2 = Label(self, {'text':'RegExp: '})
		self.entry1 = Entry(self, {'width': 30})
		self.entry2 = Entry(self, {'width': 30})

		#self.label1.pack({'side': 'left'})
		#self.entry1.pack({'side': 'left'})
		#self.entry2.pack({'side': 'top', 'side': 'left'})
		#self.canvas2.pack({'side': 'right', 'fill': 'y'})
		#self.canvas1.pack({'fill': 'both'})
		#self.but1.pack({'side': 'top', 'fill': 'y'})
		#self.label1.pack({'side': 'left'})
		#self.entry1.pack({'side': 'left'})
		#self.entry2.pack({'side': 'bottom'})
		self.label1.grid({'row': 0, 'column': 0});
		self.label2.grid({'row': 1, 'column': 0});
		self.entry1.grid({'row': 0, 'column': 1});
		self.entry2.grid({'row': 1, 'column': 1});
		self.but1.grid({'row': 0, 'column': 2, 'rowspan': 2});
		self.master.bind('<Escape>', self.exit);

app = Application()
app.mainloop()
