# fromkeys()方法用于创建一个新字典，以序列seq中的元素做字典的键，value为字典左右键对应的初始值
seq=('name','sex','age')
value=('ding','女',30)
info=dict.fromkeys(seq)
print('新的字典为：%s' %info)
info=dict.fromkeys(seq,10)
print('新的字典为：%s' %info)
info=dict.fromkeys(seq,('ding','女',30))
print('新的字典为：%s' %info)
info=dict.fromkeys(seq,value)
print('新的字典为：%s' %info)

# 把value赋值给每一个键