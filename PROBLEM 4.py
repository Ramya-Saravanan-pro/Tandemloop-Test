no = [1,2,8,9,12,46,76,82,15,20,30]
res={}
for i in range(1,10):
    res[i]=0
    for num in no:
        if num%i==0:
            res[i]+=1;
    print(res)