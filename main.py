"""
SiteDownloader executer.
"""


from controller import *
from ui import *
from storer import *
from pageparser import *
from page import *


class Main:
	status = 'inactive'

	def __init__(self):

		self.pageParser = PageParser(self)
		self.storer = Storer(self)
		self.controller = Controller(self)
		self.ui = Ui(self)

		self.ui.mainloop()

	def setStatus(self, status):
		self.status = status

Main()
