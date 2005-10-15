"""
ToDo:
	at first make to download single file

	+ Core
	* UI's API
		+ add new queue entry
	* Getter
	+ Parser
	* Storer
"""

from controller import *
from ui import *
from getter import *
from storer import *


class main:
	def __init__(self):
		self.getter = getter(self)
		self.storer = storer(self)
		self.controller = controller(self)
		self.ui = ui(self)

		self.ui.mainloop()



	def start(self):
		storer.setBasePath(ui.getBasePath())
		basePath = ui.getBasePath()
		url = ui.getFirstUrl()
		print basePath, url



main()


#basePath = re.search(r'(.*)[/\\]', __file__).group(1);
#url = 'http://localhost/index.php'

#page = getter.get(url)
#storer.store(page, url)


