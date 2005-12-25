import model.Listened as Listened

	
l = ['kuku']
s = set(l)
print id(l)
print id(s)
l.append('sad')
print id(l)
print id(s)
