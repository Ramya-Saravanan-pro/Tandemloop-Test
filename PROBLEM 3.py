a=int(input("Enter a no: "))
if a%2==0:
    a-=1
for i in range(a):
    print(2*i+1,end='')
    if i!=a-1:
        print(',',end='')