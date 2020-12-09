#pop()方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值

#语法:list.pop()
# pop方法是唯一一个既能修改列表又能返回元素值的列表方法

field=['hello','world','python','is','funny']
print(field.pop())
print('移除元素后的field：',field)

print(field.pop(3))
print('移除元素之后的field：',field)

print(field.pop(0))
print('移除元素之后的field：',field)
