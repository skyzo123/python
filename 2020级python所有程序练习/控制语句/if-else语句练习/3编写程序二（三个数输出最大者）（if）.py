a=int(input("请输入第一个数:"))
b=int(input("请输入第二个数:"))
c=int(input("请输入第三个数:"))
if a<=b:
                if b<=c:
                                print("最大的数为:",c)
                else:
                                print("最大的数为:",b)
else:
                if c>=a:
                                print("最大的数为:",c)
                else:
                                print("最大的数为:",a)

input()
