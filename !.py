d = {'ku': 'kuku', 'uk': 'ukuk'}
l = []
for i, k in d.iteritems():
	l.append([i, k])
l.append(['column', 0])
l.append(['row', 0])
print dict(l)