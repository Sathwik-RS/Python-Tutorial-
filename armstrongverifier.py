def verify(num):
  target=num
  onum=num
  digitcount=0 
  sum=0
  while(target!=0):
    if(target%10>=0):
      digitcount=digitcount+1
      target= target // 10

  while(num!=0):
    rem=num%10
    sum=sum+(rem**digitcount)
    num= num // 10    

    
  if(sum==onum):
   print("the number is amstrong")
  else:
      print("its not an amstrong number ")
   
 
       
