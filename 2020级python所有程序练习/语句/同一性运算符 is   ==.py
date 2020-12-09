# ==用来判断两个对象是否相等
# is用来判断两个变量是否指向同一个对象
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)

s=[1,2,3]
y=[1,5]
print(x is not y)
del x[2]
print(x)
y[1]=2
print(y)
print(x==y)
print(x is y)
