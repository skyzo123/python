def fun():
        s=0
        for i in range(1,21):
                t=1
                for j in range(1,i+1):
                        t=(t*j)
                print(t)
                s+=t
        return s


print(fun())


                
