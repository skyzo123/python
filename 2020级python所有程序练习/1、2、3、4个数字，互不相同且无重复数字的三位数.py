def main():
        for i in range(1,5):
                for j in range(1,5):
                        for k in range(1,5):
                                if(i!=j and j!=k and i!=k):
                                        print(i*100+j*10+k)

main()
