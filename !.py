a = ['4']
a.append('as')

try:
	print a[2]
except IndexError:
	print None
