import random;

listAll = [];
lists = [[] for i in range(5)];

#初始游戏
def initGame():
    i = 0;
    while(i < 15):
        tempInt = random.randint(1,255);
        if(tempInt not in listAll):
            listAll.append(tempInt);
            i = i + 1;
    lists[0] = listAll[0:5];
    lists[1] = listAll[5:10];
    lists[2] = listAll[10:15];

#询问
def askPlayer():
    i = 0;
    while(i <3):
        count = 0;
        while(count < 3):
            tempAll = [];
            print(lists[count]);
            answer = input("is it in?y or n\n");
            if(answer=='y'):
                if(count==0):
                    tempAll.append(lists[count+1]);
                    tempAll.append(lists[count]);
                    tempAll.append(lists[count+2]);
                elif(count==1):
                    tempAll.append(lists[count-1]);
                    tempAll.append(lists[count]);
                    tempAll.append(lists[count+1]);
                elif(count==2):
                    tempAll.append(lists[count-2]);
                    tempAll.append(lists[count]);
                    tempAll.append(lists[count-1]);
                #重新发牌
                shuffleCard(tempAll)
                break;
            count+=1;
        i+=1;    
    
#发牌
def shuffleCard(tempAll):
    lists[0]=[];
    lists[1]=[];
    lists[2]=[];
    j=0;
    while(j<3):
        k=0;
        while(k<5):
            if((j*5+k)%3==0):
                lists[0].append(tempAll[j][k]);
            elif((j*5+k)%3==1):
                lists[1].append(tempAll[j][k]);
            elif((j*5+k)%3==2):
                lists[2].append(tempAll[j][k]);
            k+=1;
        j+=1;


#初始化15个数字
initGame();

#游戏开始
print(listAll);
print("please remember one num!");

askPlayer();
    
print("the answer is");
print(lists[1][2]);

