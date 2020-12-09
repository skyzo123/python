L=[1,1,2,2,3,4,3,5,1,1]
#L.remove(1)
#print(L)
#L.remove(1)
#print(L)
#L.remove(1)
#print(L)
#L.remove(1)
#print(L)
#for e in L:
#        y=e
#        print(y)
#        if(y==1):
#                L.remove(e)
#        print(L)
length=len(L)
print(length)
i=0
while(i<len(L)):
        y=L[i]
        print(y)
        if(L[i]==1):
                L.remove(L[i])
                i=0
        else:
                i+=1
        print(L)
