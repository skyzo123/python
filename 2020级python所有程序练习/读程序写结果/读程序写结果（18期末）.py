def ff(a):
    n = len(a)
    i = 1
    j = 0
    while i<n :
        if a[j]>a[i]:
            j = i
        i+=1
    x = a[0]
    a[0]=a[j]
    a[j]=x
xx=[44,34,1,12,6,29,13]
print(xx)
ff(xx)
print(xx)
