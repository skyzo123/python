'''
for j in range(1,10):
    for i in range(1,j+1):
        print("%d*%d=%d"%(j,i,j*i),end="\t")
    print()
'''
L=[1,5,2,0,4]
for i in range(1,len(L)):
    bool = 0
    for j in range(0,len(L)-i):
        if(L[j]>L[j+1]):
            bool=1
            L[j],L[j+1]=L[j+1],L[j]
    if bool==0:
        break
    print(L)
#print(count)

