"""
ToDo:
	+ Core
	* UI's API
		+ add new queue entry
	+ Getter
	+ Parser
	+ Storer
"""

from ui import *
from getter import *
from storer import *

ui = ui()
getter = getter()
#parser = parser()
storer = storer(re.search(r'(.*)[/\\]', __file__).group(1))

url = 'http://localhost/index.php'

ui.addEntry(url)
page = getter.get(url)
storer.store(page, url)


