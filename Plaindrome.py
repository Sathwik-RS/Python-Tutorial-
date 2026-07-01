num=int(input("enter the number"))
def reverse(num):
 rev=0
 while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
 return rev

reversenum=reverse(num)
if(num==reversenum):
  print("number is a palindrome")