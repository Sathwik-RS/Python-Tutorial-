num=int(input("enter the number"))
sum=0
i=0
for i in range(num):
    if(i==0):
        continue
    if(num%i==0):
        sum=sum+i

if(sum==num):
    print(num)