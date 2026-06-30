
str1=input("enter 1")
str2=input("enter 2")

def compare(str1 ,str2 ):
 flag=0
 if(len(str1)==len(str2)):
  for i in range(len(str1)) :
   if(str1[i]==str2[i]) :
     flag=flag+1

 if(flag==len(str1)):
  print("both are equal")
 else:
  print("both are not equal")     

compare(str1,str2)