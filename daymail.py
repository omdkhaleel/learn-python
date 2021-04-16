def dow():
	fname=input('Enter a file name: ')
	fhand=open(fname)
	d=dict()
	for line in fhand:
		if line.startswith('From '):
			words=line.split()
			c=words[2]
			d[c]=d.get(c,0)+1
	print(d)
