L=[1,1.3,'2','china',['I','am','another','list']]
print("第一次分片的结果：",L[-1:-4:-1])
print(len(L))
print("小列表中的第一个元素为",L[4][0])
#当序列中的数据类型都是整数或者浮点数的时候才能求最大值和最小值
nums=[0.1,1.3,2,50]
print("nums数列的最小值为：",min(nums))
print("nums数列的最大值为：",max(nums))
greeting=list("hi")
print("greeting的结果为：",greeting)
#列表分片赋值:可以使用与原序列不等长的序列将分片替换
greeting[1:]=list("ello")
print(greeting)

#分片赋值
field=list('ae')
print("field 的结果为：",field)
#可以在不替换任何原有元素的情况下在任意位置插入新元素
#这个例子是替换了一个空分片，实际是插入一个序列
#分片赋值比append（）方法功能要强大，因为append只能在末尾进行添加
field[1:1]=list('bcd')
print(field)
boil=list('女排夺冠了')
print(boil)
boil[2:2]=list('2016年奥运会')
print(boil)

#分片赋值实现删除功能
field=list('abcde')
print(field)
field[1:4]=[]
print(field)
boil=list('女排2016年奥运会夺冠了')
print(boil)
boil[2:10]=[]
print(boil)

field=list('aeadfafafd')
field[1:0]=list('hello')
print(field)
