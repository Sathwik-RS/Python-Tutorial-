oa=int(input("enter number 1"))
ob=int(input("enter number 2"))
a=oa
b=ob
while(b!=0):
    temp=b
    b=a%b
    a=temp
lcm=(oa*ob)/a
print(lcm)