'''
def jiecheng(x):
    sum=1
    for i in range(1,x+1):
        sum*=i
    return sum
'''
def jiecheng(x):
    if x==0:return 1
    else:
        sum=jiecheng(x-1)
        return x*sum

result=jiecheng(5)
print(result)