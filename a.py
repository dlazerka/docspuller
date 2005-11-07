class A:
	__x = 'kuk'
	
	def getX(self):
		return self.__x
		
	x = property(getX)
	
print A().x
	