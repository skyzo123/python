# get()方法返回指定键的值，如果值不在字典中，就返回默认值
# get()方法的语法：dict.get(key,default=None)
student={'小萌':'1001','小智':'1002'}
print('小萌的学号为：%s' %student.get('小萌'))
st={}
# print(st['name'])
#这句输出会报错
print(st.get('name'))
# 这句输出为None
print('name的值为：%s' %st.get('name'))
