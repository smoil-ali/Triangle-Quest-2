for i in range(1,int(input())+1):
    print(sum(map(lambda x:x[1]*10**x[0],enumerate((list(range(1,i+1))+list(range(i-1,0,-1)))))))