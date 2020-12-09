def birth_to_seven(birth):
    n=birth
    L=[]
    s=""
    while(n!=0):
        m=n%7
        L.append(m)
        n=n//7
    L.reverse()
    list=[str(i) for i in L]
    list1=''.join(list)
    print(list1)

def yuanma(birth):
    n = birth
    L = []
    while (n != 0):
        m = n % 2
        L.append(m)
        n = n // 2
    while(len(L)!=32):
        L.append(0)
    L.reverse()
    list = [str(i) for i in L]
    list1 = ''.join(list)
    print(list1)


string=int(input("请输入学生出生年月日："))
birth_to_seven(string)
yuanma(string)
