def rec(L):
    if  L == [ ] : return
    L = L[ 0 : len(L)-1 ]
    print("L = ",L)
    rec( L )
    print("L :",L)
    return
X = [1,2,3]
rec( X )
print("outside rec, X =", X)
input()
