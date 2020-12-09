#count()方法用于统计某个元素在列表中出现的次数
#语法：list.count(obj)
field=['h','e','l','l','o','w','o','r','l','d']
print(field)
#统计列表中的字符个数
print('列表field中，字母o的个数：',field.count('o'))
print('列表field中，字母l的个数：',field.count('l'))
print('列表field中，字母a的个数：',field.count('a'))
listobj=[123,'hello','world',123]
listobj=[26,'hello','world',26]
print('数字26的个数：',listobj.count(26))
print('hello的个数：',listobj.count('hello'))
print(['a','c','a','f','a'].count('a'))
mix=[[1,3],5,6,[1,3],2]
print('嵌套列表mix中列表[1,3]的个数为：',mix.count([1,3]))


