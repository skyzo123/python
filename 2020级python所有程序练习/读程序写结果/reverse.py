list=[1,2,3,4,5]
def fun(a):
	low=0
	high=len(a)-1
	while low<high:
		a[low],a[high]=a[high],a[low]
		low=low+1
		high=high-1
	print(a)

fun(list)