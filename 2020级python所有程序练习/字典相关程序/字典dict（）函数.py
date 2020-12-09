# dict（）函数，通过其他映射（如其他字典）或键/值序列对建立字典
#a=str("123")
student={'name':'小萌','number':'1001'}
detail=dict(student)
print('学生详细信息：',detail)
print('学生姓名：',detail['name'])
print('学生学号：',detail['number'])

# dict()可以将序列转换为字典
student1=[{'name','小萌'},{'number','1001'},{'ding','1002'}]
print('学生详细信息：',dict(student1))

