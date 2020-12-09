c=[]
for i in range(1,6):
    c.append(2**(5-i)%10)
a=[2,3,0,5,2]
s=0
for i in range(0,5):
    s += c[i]*a[i]
s=s%10
print("余数：",s)

