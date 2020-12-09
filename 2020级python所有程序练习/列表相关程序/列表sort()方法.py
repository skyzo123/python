# sort()方法用于对原列表进行排序，如果指定参数，就是用参数指定的比较方法进行排序
# 语法：list.sort()
num=[5,8,1,3,6]
num.sort()
print('num调用sort方法后:',num)
# num本身也变了
num=[5,8,1,3,6]
n=num.sort()
print('变量n的结果是：',n)
print('列表num排序后的结果是：',num)
# sort（）方法修改了列表num，但是返回的是空值

num=[5,8,1,3,6]
n=num
n.sort()
print('变量n的结果是：',n)
print('num的结果是：',num)
# n和num指向的是同一个列表
num=[5,8,1,3,6]
n=num[:]
num.append(9)
print('append 变量n的结果是：',n)
print('append num的结果是：',num)
n.sort()
print('变量n的结果是：',n)
print('num的结果是：',num)
# 分片保留了副本，num没有变，n被排序了

num=[5,8,1,3,6]
n=sorted(num)
print('变量n的操作结果是：',n)
print('num的结果是：',num)
# num保持了原样
print(sorted('python'))

# 高级排序
field=['study','python','is','happy']
field.sort(key=len)
print('filed的结果是：',field)
field.sort(key=len,reverse=True)
print(field)
num=[5,8,1,3,6]
num.sort(reverse=True)
print(num)