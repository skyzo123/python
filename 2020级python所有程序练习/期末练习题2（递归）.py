def F(a):
    if len(a)==1:
        return(a[0])
    return(F(a[1:])-a[0])

b=[1,4,9,16]
print(F(b))
input()
