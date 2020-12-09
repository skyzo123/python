c=[]
for i in range(0,5):
        c.append(2**(6-i)%3)

a=[2,3,0,5,2]
s=0
for i in range(0,5):
        x=c.pop(0)
        y=a.pop(0)
        s+=x*y

s=s%11
print('余数:',s)
input()
