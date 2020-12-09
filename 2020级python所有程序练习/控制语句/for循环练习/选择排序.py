L=[2,5,1,0,4]
for k in range(len(L)-1):
    min=k
    for i in range(k+1,len(L)):
        if L[min]>L[i]:
            min=i
    L[k],L[min]=L[min],L[k]
    print(L)
