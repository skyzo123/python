a=[26,90,73,47,18]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i],a[i+1]=a[i+1],a[i]
print(a)


