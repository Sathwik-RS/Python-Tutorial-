n=int(input("enter the value of n"))
factorial=1
def fact(n):
            if(n==0 | n==1):
               return 1
            else:
             factorial= n*fact(n-1)
             return factorial

    

     

print(fact(n))