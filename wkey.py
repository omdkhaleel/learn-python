def wkey():
	fname = input('Enter a file name: ')
	fhand = open(fname)
	wdic={}
	for line in fhand:
		line=line.rstrip()
		words=line.split()
		wdic= {word:None for word in words}
		print(wdic)
