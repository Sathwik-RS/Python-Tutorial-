a=int(input("side 1"))
b=int(input("side 2"))
c=int(input("side 3"))

if a==b==c :
    print("it is an equilateral triangle")

elif a==b or b==c or c==a :
        print("it is an isoceles triangle")
else :
          print("it is an scalene triangle")

      

