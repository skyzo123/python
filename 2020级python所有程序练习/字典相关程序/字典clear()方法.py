# clear()方法只是清空字典，并不是删除字典，请注意和del的区别
student={'小萌':'1001','小智':'1002','小强':'1005','小张':'1006'}
print('使用clear（）方法之前，字典student中包含的元素的个数为：%d个' %len(student))
print(student)
student.clear()
print('使用clear（）方法之后，字典student中包含的元素的个数为：%d个' %len(student))
print(student)
