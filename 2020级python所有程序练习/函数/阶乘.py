def jiecheng(num):
	if num==0:return 1
	if num>0:
 		return num*jiecheng(num-1)

n=int(input("请输入一个整数："))
result=jiecheng(n)
print("%d的阶乘是%d"%(n,result))


def  Unrecursion(num):
	sum=1
	if num==1:return 1
	if num>1:
		while num>0:
			sum*=num
			num=num-1
		return sum

n=int(input("请输入一个整数："))
result=Unrecursion(n)
print("%d的阶乘是%d"%(n,result))