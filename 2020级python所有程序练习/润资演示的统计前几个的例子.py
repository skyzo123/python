# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dict1 = {'abc': 456}
# dict2 = {'abc': 123, 98.6: 37}
import re
import operator

ss = open("harry.txt").read()
listoftokens = re.split(r"[\s\"\.\t\,0-9]", ss)
#去掉r也不影响结果，\s转义字符：\s：空格\"：双引号\.：点\t：tab键\,：逗号
strlist = [s.lower() for s in listoftokens if len(s) > 3]
#推导式
dic = {}
for i in strlist:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1

t = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print(t)
