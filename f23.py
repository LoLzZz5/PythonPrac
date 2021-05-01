def f23(x):
	c=[]
	for row in x:
		for elem in row[:]:
			if elem == None:
				row.remove(elem)
	for row in x:
		if len(row)==0:
			x.remove(row)
	unique=[]
	for row in x:
		if row not in unique:
			unique.append(row)
	for row in unique:
		proc=''
		for i in row[0]:
			proc+=i
		proc=proc[0:6]
		proc=float(proc)
		p='{:,.2f}'.format(float(proc))
		p=p[2:]+'%'
		if p[0]=='0':
			p=p[1:]
		name=''
		for i in row[1]:
			name+=i
		name = name.replace(',', '')
		name = name[::-1]
		name1 = name[2:4]
		name1 = name1[::-1]
		name = name[5:]
		name = name[::-1]
		name+=' '+name1
		g=''
		for i in row[2]:
			g+=i
		if g[0]=='д':
			g='Да'
		else:
			g='Нет'
		d=[]
		d.insert(0, g)
		d.insert(0, name)
		d.insert(0, p)
		c.insert(0, d)
	c=c[::-1]
	return c


x=[[None, '0.009', 'Кемев, Я.У.', 'нет'], 
   [None, '0.689', 'Ламли, М.Е.','да'],
   [None, '0.689', 'Ламли, М.Е.','да'],
   [None, None, None, None],
   [None,'0.139', 'Добберг, Ю.Г.', 'да'],
   [None, '0.689', 'Ламли, М.Е.','да']]
print(f23(x))