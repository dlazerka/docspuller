"""
ToDo:

"""


from controller import *
from ui import *
from getter import *
from storer import *
from pageparser import *


class Main:
	def __init__(self):

		self.parser = PageParser(self)
		self.getter = Getter(self)
		self.storer = Storer(self)
		self.controller = Controller(self)
		self.ui = Ui(self)

		self.ui.mainloop()

Main()
