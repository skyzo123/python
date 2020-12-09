def tt(a):
    n = len(a)
    i = 1
    while i<n :
        j=0
        while j<n-i:
            if a[j]<a[j+1]:
                t = a[j]
                a[j]=a[j+1]
                a[j+1]=t
            j+=1
        i+=1
xx=[44,34,1,12,6,29,13]
print(xx)
tt(xx)
print(xx)

a="20"
b='18'
print(a+b)