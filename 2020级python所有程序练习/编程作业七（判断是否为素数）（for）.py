def main():
                key = int(input("请输入一个整数:"))
                for i in range(2,key):
                                if key % i==0:
                                                print("这个数不是素数！")
                                                break
                else:
                                print("这个数"+str(key)+"是素数")

main()
input()
                                
