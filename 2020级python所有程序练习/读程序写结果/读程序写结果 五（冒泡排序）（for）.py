a=[26,90,73,47,18]
# for i in range(len(a)-1):
#                 if a[i]>a[i+1]:
#                                 a[i],a[i+1]=a[i+1],a[i]
#                                 print(a)

def fun(list):
    i=1
    while i<5:
        for j in range(len(list) - 1):
            if list[j] < list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
        i=i+1
    print(list)

def fun2(list):
    i = 1
    while i < 5:
        j=0
        while j<len(list)-1:
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            j=j+1
        i = i + 1
    print(list)
fun(a)
fun2(a)


