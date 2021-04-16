def dow():
	fname=input('Enter a file name: ')
	fhand=open(fname)
	d=dict()
	for line in fhand:
		if line.startswith('From '):
			words=line.split()
			c=words[1]
			d[c]=d.get(c,0)+1
	print(max(d,key=d.get))
	print(max(d.values()))
