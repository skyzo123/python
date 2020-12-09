def shuixianhuashu():
	i=0
	sum=0
	l=[]
	for i in range(100,1000):
		m=i
		while m != 0:
			l.append(m%10)
			m= m // 10
		# sum=l[0]**3+l[1]**3+l[2]**3
		for item in l:
			sum+=item**3
		if sum==i:
			print("%d是水仙花数" %i )
		l=[]
		sum=0


shuixianhuashu()

