'''def happy(x):
    y=x*x*x
    return y

def compare(a,b):
    if a>b:
        return a
    else:
        return b

result=happy(3)
print(result)
max=compare(7,5)
print(max)
'''
#水仙花数：三位数，某一个三位数，三个位上的整数的立方和==数本身，
def water():
    for x in range(100,1000):
        L=[]
        i=x
        sum=0
        while i!=0:
            j=i%10
            i=i//10
            L.append(j)
        for k in L:
            sum+=k**3
        if sum==x:
            print("%d是水仙花数"%x)



water()