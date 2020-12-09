x=10
s=0
while x>2:
    if(x%2!=0):
        x=x-1
        continue
    s+=x
    x=x-1
print(x,s)

