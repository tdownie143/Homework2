def main():
	Ninety_Nine_Bottles_Of_Beer()
	
def Ninety_Nine_Bottles_Of_Beer():
	for x in reversed(xrange(100)):
		if (x > 1):
			g = str(x)
			l = str(x-1)
			print(g+" bottles of beer on the wall, "+g+"bottles of beer. Take one down, pass it around, "+l+"bottles of beer on the wall")
		elif (x == 1):
			g = str(x)
			print(g+" bottles of beer on the walle, "+g+"bottle of beer. Take one down, pass it around, no more bottles of beer on the wall")
main()