# setdefault()方法和get()方法类似，用于获得与给定键相关联的值。如果键不存在于字典中，就会添加键并将值设为默认值
# 语法：dict.setdefault(key,default=None)
student={'小萌':'1001','小智':'1002'}
print('小强的键值为：%s' %student.setdefault(('小强')))
print('小智的键值为：%s' %student.setdefault(('小智')))
print('student字典新值为：%s' %student)