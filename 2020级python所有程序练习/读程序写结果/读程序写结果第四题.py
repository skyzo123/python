def main():
    a=[50,75,53,92,77,64,79,21]
    s=[0]*10
    for i in range(len(a)):
        k=a[i]//10
        s[k]=s[k]+1
    m=s[0]
    k=1
    while k<10:
        if s[k]!=0:
            print("%d"%s[k])
        if s[k]>m:
            m=s[k]
        k+=1
    print("%d"%m)

main()
input()
