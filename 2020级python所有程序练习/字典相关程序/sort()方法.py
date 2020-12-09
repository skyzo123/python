# 1.
# sorted函数按key值对字典排序
# 先来基本介绍一下sorted函数，sorted(iterable, key, reverse)，sorted一共有iterable, key, reverse这三个参数。
# 其中iterable表示可以迭代的对象，例如可以是
# dict.items()、dict.keys()等，key是一个函数，用来选取参与比较的元素，
# reverse则是用来指定排序是倒序还是顺
# 序，reverse = true则是倒序，reverse = false时则是顺序，默认时reverse = false。
# 要按key值对字典排序，则可以使用如下语句：
#d={'lilee':25,'wangyan':21,'liqun':32,'lidaming':19}
#sorted(d.keys())
#
#
# 直接使用sorted(d.keys())
# 就能按key值对字典排序，这里是按照顺序对key值排序的，如果想按照倒序排序的话，则只要将reverse置为true即可。
#
# 2.
# sorted函数按value值对字典排序
#
# 要对字典的value排序则需要用到key参数，在这里主要提供一种使用lambda表达式的方法，如下：
#
#d={'lilee':25,'wangyan':21,'liqun':32,'lidaming':19}
#sorted(d.items(),key=lambda item:item[1])
# 这里的d.items()
# 实际上是将d转换为可迭代对象，迭代对象的元素为 （‘lilee’, 25）、（‘wangyan’, 21）、（‘liqun’, 32）、（‘lidaming’, 19），
# items()
# 方法将字典的元素
# 转化为了元组，而这里key参数对应的lambda表达式的意思则是选取元组中的第二个元素作为比较参数
# （如果写作key = lambda item: item[0]
# 的话则是选取第一个元素作为比较对象，也就是key值作为比较对象。lambda x: y中x表示输出参数，y表示lambda
# 函数的返回值），
# 所以采用这种方法可以对字典的value进行排序。注意排序后的返回值是一个list，而原字典中的名值对被转换为了list中的元组。
import re
import operator
ss ="h e l l o, w o r l d!a a"
listoftokens = re.split(r"[\s\"\.\t\,!0-9]", ss)
dic = {}
for s in listoftokens:
    s = s.lower()
    if len(s) >=1:
        if s in dic:
            dic[s] = dic[s] + 1
        else:
            dic[s] = 1
t = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(t)
