def g(L):
        m=0
        for i in range(0,len(L)):
                if L[i]>L[m]:
                        m=i
                        L[0],L[m]=L[m],L[0]

L1=[4,5,1,2,0]
g(L1)
print(L1)
