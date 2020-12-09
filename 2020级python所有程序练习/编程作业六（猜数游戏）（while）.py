import random
def main():
                key = random.randint(0,10)
                while 1==1:
                                guess=int(input("请输入一个整数:"))
                                if guess < key:
                                                print("太小")
                                elif guess==key:
                                                print("恭喜！你猜中了！")
                                                break
                                else:
                                                print("太大")

main()
input()
#print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20  
#print random.randint(20, 20)  #结果永远是20  
#print random.randint(20, 10)  #该语句是错误的。下限必须小于上限                                
                                                 
                
                                
                

               
                
                
