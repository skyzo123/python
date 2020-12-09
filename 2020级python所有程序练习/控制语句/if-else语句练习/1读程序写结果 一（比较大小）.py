def main():
    a,b,x,y=4,2,3,8
    if x>0:
        a=a+1
    if x>y:
        b=b+1
    elif x==y:
        b=5
    else:
        b=2*x
    print(a,b)

main()

