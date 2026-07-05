a=int(input("enter number 1"))
b=int(input("enter number 2"))
while(b!=0):
    temp=b
    b=a%b
    a=temp
print(a)