#有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第
#3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后
#问第一个人，他说是10岁。请问第五个人多大？
def age(n):
	if n==1:return 10
	if n>1:
		return age(n-1)+2


xuhao=int(input("请输入最后一个人的编号："))
result=age(xuhao)
print("第%d个人的岁数为%d" % (xuhao,result))