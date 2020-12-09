# 序列赋值
x,y,z=1,2,3
print(x,y,z)

# 交换变量的值
x,y,z=1,2,3
x,y=y,x
print(x,y,z)

nums=1,2,3
print(nums)
x,y,z=nums
print(x)
print(x,y,z)

student={'name':'小萌','number':'1001'}
key,value=student.popitem()
print(key)
print(value)

# 链式赋值
x=y=z=10
print(x)

# 增量赋值
x=5
x+=1
print(x)
x-=2
print(x)
x*=2
print(x)
x/=4
print(x)
#增量赋值还适用于字符串的连接
field='hello,'
field+='world'
print(field)
field*=2
print(field)
