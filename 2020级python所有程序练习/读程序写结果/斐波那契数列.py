def fun():
	i=0
	l=[]
	while i<20:
		if i==0 or i==1:
			l.append(1)
		else:
			l.append(l[i-1]+l[i-2])
		i=i+1
	print(l)

fun()
def fundigui(n):
	l=[]
	sum=0
	if n==1 or n==2:
		sum=1
		return sum
	else:
		sum=fundigui(n-1)+fundigui(n-2)
		return sum

print(fundigui(10))