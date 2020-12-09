# update()方法用于把字典dict2的键值对更新到dict里
# 语法：dict.update(dict2)
student={'小萌':'1001','小智':'1002'}
student2={'小李':'1003'}
print('原student字典为：%s' %student)
student.update(student2)
print('新student字典为：%s' %student)
student3={'小李':'1005'}
student.update(student3)#对键相同项进行覆盖
print('原student字典为：%s' %student)