#extend()方法用于在列表末尾一次性追加另一个序列中的多个值
#语法：list.extend(seq)
a=['hello','world']
b=['python','is','funny']
a.extend(b)
a.extend([1,2,3])
print(a)

#extend()方法和序列相加的区别
#序列相加
a=['hello','world']
b=['python','is','funny']
print(a+b)
print(a)

#用分片赋值实现和extend()相同的结果
a=['hello','world']
b=['python','is','funny']
a[len(a):]=b
print(a)


