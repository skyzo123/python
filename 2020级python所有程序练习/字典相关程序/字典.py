scores={"zhangsan":95,"lisi":75,"wangwu":85}
print(scores["zhangsan"])
scores["zhangsan"]=96
print(scores)
print(scores["zhangsan"])
del scores["zhangsan"]
print(scores)
del scores
scores={}
print(scores)