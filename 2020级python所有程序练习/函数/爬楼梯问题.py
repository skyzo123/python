def func(m):
    floor=[1,2,4]
    for i in range(3,m):
        floor.append(floor[i-1]+floor[i-2]+floor[i-3])
    print(floor)
s=int(input("请输入台阶数n："))
func(s)


# 递归函数写法
def digui(m):
    if m==1:sum=1
    elif m==2:sum=2
    elif m==3:sum=4
    else:
        for i in range(3,m):
            sum=digui(m-1)+digui(m-2)+digui(m-3)
    return sum

s=int(input("请输入台阶数n："))
result=digui(s)
print(result)


