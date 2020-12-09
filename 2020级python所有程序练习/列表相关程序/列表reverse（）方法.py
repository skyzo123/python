# reverse()方法用于反向列表中的元素
# 语法：list.reverse()
num=[1,2,3]
print('列表反转前num：',num)
num.reverse()
print('列表反转后：',num)

num=[1,2,3]
print('使用reversed函数翻转结果：',list(reversed(num)))
print('num的结果是：',num)
# num保持了原样