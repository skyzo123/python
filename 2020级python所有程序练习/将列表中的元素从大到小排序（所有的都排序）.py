def g(L):
        m=0
        n=0
        for i in range(0,len(L)-1):
                for j in range(i,len(L)):
                        if L[j]>L[i]:
                                m=L[j]
                                n=L[i]
                                L[i],L[j]=m,n
                print(L)

L1=[4,5,1,2,0]
L2=[7,9,4,5,2,1,3]
g(L1)
g(L2)
print(L1)
print(L2)
